from pyperclip import copy

from offsync.api import HaveIBeenPwned
from offsync.security import get_master_password, generate_profile_password
from offsync.storage import profiles, create_profile, delete_profile, update_profile
from offsync.template import Profile
from offsync.ui import _Table, Input, Print

PROMPT_PASSWORD = False


def usage() -> None:
    """Display usage information for the offsync command-line tool."""

    Print.info("""
USAGE: offsync [Option] (add, remove, update, prompt, pwned, help)

Arguments:""")

    Print.success("""
    add            add new profile
    add c          add multiple profiles at once""")

    Print.fail("""
    remove         remove new profile
    remove c       remove multiple profiles at once""")

    Print.warning("""
    update         change profile counter to update password
    pwned          check if generated passwords have been breached
    prompt         show password in clear text
    help           Show this help menu
""")


def list_profiles(*, vp, qp, pp) -> None:
    """
    Display a list of user profiles in a formatted table.

    Args:
        vp (bool): View Prompt flag.
        qp (bool): Quit Prompt flag.
        pp (bool): Password Prompt flag.
    """

    table = _Table(vp=vp, qp=qp, pp=pp)

    for profile in profiles():
        table.add_row(profile.__dict__)

    table.tabulate()


def select_profile(only_id: bool = False) -> None | int | Profile:
    """
    Prompt the user to select a profile from the table.

    Args:
        only_id (bool): Flag to indicate if only the ID should be returned.

    Returns:
        None | int | Profile: The selected profile, its ID, or None.
    """

    ask = Input().selection

    if ask == "q" or ask == "quit" or ask == "exit":
        copy("")
        exit(0)

    if only_id is False:
        if ask == "v" or ask == "view":
            list_profiles(vp=True, qp=True, pp=True)
            return None

        if ask == "p" or ask == "prompt":
            global PROMPT_PASSWORD
            PROMPT_PASSWORD = not PROMPT_PASSWORD
            return None

    try:
        for profile in profiles():
            if profile._id == int(ask):
                if only_id:
                    return profile._id
                return profile
    except ValueError:
        Print.fail("Invalid Input!")
        return None


def add_profile() -> None:
    """Prompt the user to add a new profile."""

    site = Input("Site", default="None").string
    username = Input("Username / E-Mail", default="None").string
    counter = str(Input("Counter", default=1).integer)
    length = str(Input("Length", default=16).integer)

    create_profile(Profile(0, site, username, counter, length))


def add_profiles() -> None:
    """Prompt the user to add multiple profiles."""

    while True:
        add_profile()
        ask = Input("\nContinue (Y/n)", default="y", show_default=False).string.lower().strip()
        print()

        if ask == "n" or ask not in ["y", ""]:
            list_profiles(vp=False, qp=False, pp=False)
            break


def remove_profile() -> None:
    """Prompt the user to remove a profile."""

    list_profiles(vp=False, qp=True, pp=False)
    _id = select_profile(only_id=True)

    if _id is not None:
        delete_profile(str(_id))
    else:
        Print.warning("[*] Delete Operation Aborted!")
        exit(2)

    print()
    list_profiles(vp=False, qp=False, pp=False)


def remove_profiles() -> None:
    """Prompt the user to remove multiple profiles."""

    list_profiles(vp=False, qp=False, pp=False)
    Print.warning("\nEnter S.No. Of All Profiles You Want To Delete Separated By Coma ','")
    Print.warning("For Example: 1, 2, 3, 4")
    Print.fail("Note: Any Non-Numeric Value Will Terminate The Process")

    try:
        ids = [i if i.isdigit() else int(i) for i in Input("\n> ").string.replace(" ", "").split(",")]
    except ValueError as e:
        Print.fail(f"\nInvalid Input: {e}")
        exit(1)

    for _id in ids:
        delete_profile(_id)
    list_profiles(vp=False, qp=False, pp=False)


def get_password(prompt: bool = False) -> None:
    """
    Generate and copy a profile password to the clipboard.

    Args:
        prompt (bool): Flag to indicate if the password should be printed.
    """

    global PROMPT_PASSWORD
    PROMPT_PASSWORD = prompt
    mp_hash = get_master_password()
    list_profiles(vp=True, qp=True, pp=True)

    while True:
        profile = select_profile()
        if profile is None: continue
        passwd = generate_profile_password(profile, mp_hash)
        copy(passwd)
        if PROMPT_PASSWORD: print(passwd)
        Print.info("Copied To Clipboard")


def change_password() -> None:
    """Prompt the user to change a profile's password."""

    list_profiles(vp=False, qp=True, pp=False)
    profile = select_profile()
    if profile is None: exit(2)
    Print.warning("> Leave field empty if you don't want to change something\n")

    site = Input("Site").string
    username = Input("Username / E-Mail").string
    counter = Input("Counter").integer
    length = Input("Length").integer

    if counter is not None:
        counter = str(counter)
    if length is not None:
        length = str(length)

    update_profile(Profile(profile._id, site, username, counter, length))
    list_profiles(vp=False, qp=False, pp=False)


def pwned_profiles() -> None:
    """Display a list of profiles with breached passwords in a table format."""

    table = _Table(vp=False, qp=False, pp=False)
    pwned_ids = HaveIBeenPwned().get_pwned_profile_ids()

    if len(pwned_ids):
        for profile in profiles():
            if profile._id in pwned_ids:
                table.add_row(profile.__dict__)
        table.tabulate()
        Print.fail("Critical: These Profile's Password Have Been Breached. Update Them Now And Check Again")
    else:
        table.tabulate()
        Print.info("Safe: Passwords wasn't found in any data breach")
