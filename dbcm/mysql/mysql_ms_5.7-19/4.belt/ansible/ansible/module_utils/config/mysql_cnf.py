import ConfigParser

class Mycnf(ConfigParser.ConfigParser):

    def __init__(self, path):
        self.path = path
        ConfigParser.ConfigParser.__init__(self)
        self.read(self.path)

    """
    (bool) has_option(section, option)
    (bool) has_section(section)
    set(section, option, value)             NoSectionError
    (bool) remove_option(section, option)     NoSectionError
    (list) options(section)                   NoSectionError
    (list) sections()
    add_section(section)                    DuplicateSectionError
    (bool) remove_section(section)
    get(section_name,option_name)
    """

    def update(self):
        self.write(open(self.path,"w"))