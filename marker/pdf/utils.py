from typing import Optional

import filetype

from marker.settings import settings


def find_filetype(fpath):
    kind = filetype.guess(fpath)

    mimetype = kind.mime

    # Get extensions from mimetype
    # The mimetype is not always consistent, so use in to check the most common formats
    if "pdf" in mimetype:
        return "pdf"
    #elif "epub" in mimetype:
    #    return "epub"
    #elif "mobi" in mimetype:
    #    return "mobi"
    elif mimetype in settings.SUPPORTED_FILETYPES:
        return settings.SUPPORTED_FILETYPES[mimetype]
    else:
        print(f"Found nonstandard filetype {mimetype}")
        return "other"


def font_flags_decomposer(flags: Optional[int]) -> str:
    if flags is None:
        return ""

    flag_descriptions = []
    if flags & (1 << 0):  # PDFFONT_FIXEDPITCH
        flag_descriptions.append("fixed_pitch")
    if flags & (1 << 1):  # PDFFONT_SERIF
        flag_descriptions.append("serif")
    if flags & (1 << 2):  # PDFFONT_SYMBOLIC
        flag_descriptions.append("symbolic")
    if flags & (1 << 3):  # PDFFONT_SCRIPT
        flag_descriptions.append("script")
    if flags & (1 << 5):  # PDFFONT_NONSYMBOLIC
        flag_descriptions.append("non_symbolic")
    if flags & (1 << 6):  # PDFFONT_ITALIC
        flag_descriptions.append("italic")
    if flags & (1 << 16): # PDFFONT_ALLCAP
        flag_descriptions.append("all_cap")
    if flags & (1 << 17): # PDFFONT_SMALLCAP
        flag_descriptions.append("small_cap")
    if flags & (1 << 18): # PDFFONT_FORCEBOLD
        flag_descriptions.append("bold")
    if flags & (1 << 19): # PDFFONT_USEEXTERNATTR
        flag_descriptions.append("use_extern_attr")

    return "_".join(flag_descriptions)