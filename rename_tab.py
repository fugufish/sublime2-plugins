import sublime, sublime_plugin, os, shutil

class RenameTabCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.window().show_input_panel("Rename Tab:", "", lambda s: self.rename(s), None, None)
  
  def rename(self, new_file):
    old_file = self.view.file_name()
    if old_file is None:
      return
    file_dir, old_file_name = old_file.rsplit(os.sep, 1)
    if len(new_file) is 0:
      return
    if self.view.is_loading():
      return
    if self.view.is_read_only():
      return
    if(new_file == old_file):
      return
    new_file = file_dir + os.sep + new_file
    shutil.copyfile(old_file, new_file)
    if os.path.isfile(new_file):
      self.view.window().run_command("open", new_file)
      self.view.window().run_command("close")
      if old_file.endswith(".py"):
        os.remove(old_file + "c")
      os.remove(old_file)
     