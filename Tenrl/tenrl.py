import tcod

def main():
	screen_width = 80
	screen_height = 50
	

	font_path = 'arial10x10.png'
	font_flags = tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD
	tcod.console_set_custom_font(font_path, font_flags)

	window_title = "tenrl"
	fullscreen = False
	tcod.console_init_root(screen_width, screen_height, window_title, fullscreen)

	while not tcod.console_is_window_closed():
		tcod.console_set_default_foreground(0, tcod.white)
		tcod.console_put_char(0, 1, 1, '@', tcod.BKGND_NONE)
		tcod.console_flush()
		
		key = tcod.console_check_for_keypress()
		
		if key.vk == tcod.KEY_ESCAPE:
			return True
			
if __name__ == '__main__':
	main()

