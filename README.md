ClassToPath
===========

Simple plugin to Sublime Text 2 editor to replace the underscores in a classname to slashes for the goToAnything module.

Install
=======

The easiest way to install this is with [Package Control](http://wbond.net/sublime_packages/package_control).

Usage
=====

To search for the class file press <kbd>Ctrl+Shift+O</kbd>.

Note: The Plugin searches in the selection for a valid Class name and then in the clipboard, if the selection contains no valid class name.


Example
=======

Suppose the following directory tree of your Project:

	app/
		code/
			core/
				Mage/
					Checkout/
						Block/
							Cart.php
		design/
			frontend/
				base/
					default/
						template/
							checkout/
								cart.phtml
    


If you select the class in "cart.phtml" or the class name is in the clipboard, you can press <kbd>Ctrl+Shift+O</kbd> to open the <kbd>Goto file</kbd> overlay with the converted Class name.
    
    
Customization
=============
Its Possible to customize the plugin.
If you want the plugin under another shortcut, just put this into your keybinding file.

	{ "keys": ["super+shift+o"], "command": "classtopath" }
	
It`s also possible to change the separator and the replacement text for the classes.
Just add and modify this in your User Settings

	"class_to_path_separator": "_",
	"class_to_path_replacement": "/"