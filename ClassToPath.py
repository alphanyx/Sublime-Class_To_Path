import sublime, sublime_plugin, re

RE_CHECK_EXPR = '^[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*$';
SETTINGS_FILE = 'ClassToPath.sublime-settings';

class ClasstopathCommand(sublime_plugin.TextCommand):
	def run(self, command):
		className = False;

		for sel in self.view.sel():
			tmpClassName = self.view.substr(sel);
			if re.match(RE_CHECK_EXPR, tmpClassName):
				className = tmpClassName;

		if not className:
			tmpClassName = sublime.get_clipboard();
			if re.match(RE_CHECK_EXPR, tmpClassName):
				className = tmpClassName;

		if className:
			settings = self.view.settings();

			separator = "_";
			if settings.get('class_to_path_separator'):
				separator = settings.get('class_to_path_separator');

			replacement = "/";
			if settings.get('class_to_path_replacement'):
				replacement = settings.get('class_to_path_replacement');

			convertedClassName = className.replace(separator,replacement);
			self.view.window().run_command("show_overlay", {"overlay": "goto", "text": convertedClassName})
		else:
			sublime.error_message("Couldn't find Class Name in selection or in the clipboard!");
