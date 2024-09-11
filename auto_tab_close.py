import sublime
import sublime_plugin

class CloseSpecialTabsOnSwitchCommand(sublime_plugin.EventListener):
    def on_deactivated(self, view):
        if not view.is_valid():
            return
        
        self.close_special_tabs(view)

    def close_special_tabs(self, view):
        # Get the file name of the current view
        file_name = view.file_name()

        # If the file name is None (unsaved file), use the view name (typically the title shown in the tab)
        if not file_name:
            file_name = view.name()

        # Define the prefixes that should trigger closing
        settings = sublime.load_settings('AutoTabClose.sublime-settings')
        prefixes = settings.get('prefixes', [])

        # Check if the tab name starts with any of the special prefixes
        if file_name and any(file_name.startswith(prefix) for prefix in prefixes):
            if view.is_valid() and view.window():
                # Close the tab if the name matches
                # print("closing", file_name)
                view.close()
