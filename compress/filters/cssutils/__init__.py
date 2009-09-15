from compress.filter_base import FilterBase
try:
    import cssutils
except ImportError:
    print "You need to install cssutils, try easy_install cssutils"
    pass

class CSSMinFilter(FilterBase):
    def __init__(self,**kwargs):
        pass
    def filter_css(self, css):
        p = cssutils.CSSParser()
        cssutils.ser.prefs.useMinified()
        sheet = p.parseString(css)
        return sheet.cssText