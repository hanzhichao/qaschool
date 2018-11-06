from django import forms
from django.conf import settings
from django.contrib.admin import widgets as admin_widgets
from django.forms.utils import flatatt
from django.utils.html import conditional_escape

try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text
from django.utils.safestring import mark_safe


class EditorMdWidget(forms.Textarea):
    def __init__(self, attrs=None):
        super(EditorMdWidget, self).__init__(attrs)

    def build_attrs(self, base_attrs, extra_attrs=None, **kwargs):
        attrs = dict(base_attrs, **kwargs)
        if extra_attrs:
            attrs.update(extra_attrs)
        return attrs

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(self.attrs, attrs, name=name)
        html = """
            <div id="%(id)s_editormd" class="editormd" style="z-index:1001;">
                <textarea %(attrs)s style="display:none;">%(body)s</textarea>
            </div>
            <script type="text/javascript">
                var ee = {
                    'jQuery': (typeof window.django != 'undefined') ? django.jQuery : jQuery.noConflict(true)
                };

                (function ($) {
                    $(document).ready(function () {
                        var editor = editormd({
                            id: '%(id)s_editormd',
                            path: '%(path)s',
                            height: 400,
                            onfullscreen: function () {
                                console.log("onfullscreen =>", this, this.id, this.settings);
                                $('.editormd').hide()
                                $('#' + this.id).show()
                            },
                            onfullscreenExit: function () {
                                console.log("onfullscreen =>", this, this.id, this.settings);
                                $('#' + this.id).hide()
                                $('.editormd').show()
                            },
                            imageUpload: true,
                            imageFormats: ["jpg", "jpeg", "gif", "png", "bmp", "webp"],
                            imageUploadURL: "/editormd/upload/",
                        });
                    });
                })(ee.jQuery);
            </script>
            """ % {
            'path': settings.STATIC_URL + 'editor.md/lib/',
            'attrs': flatatt(final_attrs),
            'body': conditional_escape(force_text(value)),
            'id': attrs['id'],
        }
        return mark_safe(html)

    class Media:
        css = {'all': ('editor.md/css/editormd.min.css',)}
        js = (
            'jquery.min.js',
            'editor.md/editormd.min.js',
        )


class AdminEditorMdWidget(EditorMdWidget, admin_widgets.AdminTextareaWidget):
    def __init__(self, attrs=None):
        super(AdminEditorMdWidget, self).__init__(attrs)
