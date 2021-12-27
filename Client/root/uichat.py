''' 1. '''
# Add
if app.ENABLE_CHATTING_WINDOW_RENEWAL:
	import os
	import uiCommon
	import uiScriptLocale
	import cPickle
	import player

''' 2. '''
# Search @ class ChatWindow
	EDIT_LINE_HEIGHT = 25

# Add below
	if app.ENABLE_CHATTING_WINDOW_RENEWAL:
		EDIT_LINE_HIDE_HEIGHT = 20

''' 3. '''
# Search @ class ChatWindow.__init__
			imgChatBarLeft = ui.ImageBox()
			imgChatBarLeft.SetParent(self.btnChatSizing)
			imgChatBarLeft.AddFlag("not_pick")
			imgChatBarLeft.LoadImage("d:/ymir work/ui/pattern/chat_bar_left.tga")
			imgChatBarLeft.Show()
			self.imgChatBarLeft = imgChatBarLeft

			imgChatBarRight = ui.ImageBox()
			imgChatBarRight.SetParent(self.btnChatSizing)
			imgChatBarRight.AddFlag("not_pick")
			imgChatBarRight.LoadImage("d:/ymir work/ui/pattern/chat_bar_right.tga")
			imgChatBarRight.Show()
			self.imgChatBarRight = imgChatBarRight

			imgChatBarMiddle = ui.ExpandedImageBox()
			imgChatBarMiddle.SetParent(self.btnChatSizing)
			imgChatBarMiddle.AddFlag("not_pick")
			imgChatBarMiddle.LoadImage("d:/ymir work/ui/pattern/chat_bar_middle.tga")
			imgChatBarMiddle.Show()
			self.imgChatBarMiddle = imgChatBarMiddle

# Replace with
		if app.ENABLE_CHATTING_WINDOW_RENEWAL:
			imgChatBarLeft = ui.ImageBox()
			imgChatBarLeft.SetParent(self.btnChatSizing)
			imgChatBarLeft.AddFlag("not_pick")
			imgChatBarLeft.LoadImage("d:/ymir work/ui/chat/chat_linebar_left.tga")
			imgChatBarLeft.Show()
			self.imgChatBarLeft = imgChatBarLeft

			imgChatBarRight = ui.ImageBox()
			imgChatBarRight.SetParent(self.btnChatSizing)
			imgChatBarRight.AddFlag("not_pick")
			imgChatBarRight.LoadImage("d:/ymir work/ui/chat/chat_linebar_right.tga")
			imgChatBarRight.Show()
			self.imgChatBarRight = imgChatBarRight

			imgChatBarMiddle = ui.ExpandedImageBox()
			imgChatBarMiddle.SetParent(self.btnChatSizing)
			imgChatBarMiddle.AddFlag("not_pick")
			imgChatBarMiddle.LoadImage("d:/ymir work/ui/chat/chatmenutab_line.tga")
			imgChatBarMiddle.Show()
			self.imgChatBarMiddle = imgChatBarMiddle

			btnChatTab = ui.Button()
			btnChatTab.SetParent(self.btnChatSizing)
			btnChatTab.SetUpVisual("d:/ymir work/ui/chat/chatmenutab_down.tga")
			btnChatTab.SetOverVisual("d:/ymir work/ui/chat/chatmenutab_down.tga")
			btnChatTab.SetDownVisual("d:/ymir work/ui/chat/chatmenutab_down.tga")
			btnChatTab.SetToolTipText(uiScriptLocale.CHATTING_SETTING_TALKING, 0, -23)
			btnChatTab.Show()
			btnChatTab.Down()
			self.btnChatTab = btnChatTab

			btnChatSettingOption = ui.Button()
			btnChatSettingOption.SetParent(self.btnChatSizing)
			btnChatSettingOption.SetUpVisual("d:/ymir work/ui/chat/btn_option01_default.tga")
			btnChatSettingOption.SetOverVisual("d:/ymir work/ui/chat/btn_option01_over.tga")
			btnChatSettingOption.SetDownVisual("d:/ymir work/ui/chat/btn_option01_down.tga")
			btnChatSettingOption.SetToolTipText(localeInfo.CHATTING_SETTING_SETTING, 0, -23)
			btnChatSettingOption.SetEvent(ui.__mem_func__(self.__SettingOptionWndOpen))
			btnChatSettingOption.Show()
			self.btnChatSettingOption = btnChatSettingOption

			self.wndChatSettingOption = ChatSettingWindow(self)
		else:
			imgChatBarLeft = ui.ImageBox()
			imgChatBarLeft.SetParent(self.btnChatSizing)
			imgChatBarLeft.AddFlag("not_pick")
			imgChatBarLeft.LoadImage("d:/ymir work/ui/pattern/chat_bar_left.tga")
			imgChatBarLeft.Show()
			self.imgChatBarLeft = imgChatBarLeft

			imgChatBarRight = ui.ImageBox()
			imgChatBarRight.SetParent(self.btnChatSizing)
			imgChatBarRight.AddFlag("not_pick")
			imgChatBarRight.LoadImage("d:/ymir work/ui/pattern/chat_bar_right.tga")
			imgChatBarRight.Show()
			self.imgChatBarRight = imgChatBarRight

			imgChatBarMiddle = ui.ExpandedImageBox()
			imgChatBarMiddle.SetParent(self.btnChatSizing)
			imgChatBarMiddle.AddFlag("not_pick")
			imgChatBarMiddle.LoadImage("d:/ymir work/ui/pattern/chat_bar_middle.tga")
			imgChatBarMiddle.Show()
			self.imgChatBarMiddle = imgChatBarMiddle

''' 4. '''
# Search @ class ChatWindow.__init__
		self.Refresh()

# Add below
		if app.ENABLE_CHATTING_WINDOW_RENEWAL:
			self.RefreshChatWindow()

''' 5. '''
# Search @ class ChatWindow.__RegisterChatColorDict
		for colorItem in CHAT_COLOR_DICT.items():

# Add above
		if app.ENABLE_CHATTING_WINDOW_RENEWAL:
			CHAT_COLOR_DICT.update({
				chat.CHAT_TYPE_EXP_INFO : colorInfo.CHAT_RGB_INFO,
				chat.CHAT_TYPE_ITEM_INFO : colorInfo.CHAT_RGB_INFO,
				chat.CHAT_TYPE_MONEY_INFO : colorInfo.CHAT_RGB_INFO,
			})

''' 6. '''
# Search @ class ChatWindow.Destroy
		self.btnChatSizing = 0

# Add below
		if app.ENABLE_CHATTING_WINDOW_RENEWAL:
			self.btnChatTab = None
			self.btnChatSettingOption = None

			if self.wndChatSettingOption:
				self.wndChatSettingOption.Close()
				self.wndChatSettingOption = None

''' 7. '''
# Search @ class ChatWindow.OpenChat
		self.Refresh()

# Add below
		if app.ENABLE_CHATTING_WINDOW_RENEWAL:
			self.RefreshChatWindow()

''' 8. '''
# Search @ class ChatWindow.CloseChat
		self.Refresh()

# Add below
		if app.ENABLE_CHATTING_WINDOW_RENEWAL:
			self.RefreshChatWindow()

''' 9. '''
# Search @ class ChatWindow.__RefreshSizingBar
			self.imgChatBarLeft.SetPosition(0, 0)
			self.imgChatBarRight.SetPosition(width - 64, 0)
			self.imgChatBarMiddle.SetPosition(64, 0)
			self.imgChatBarMiddle.SetRenderingRect(0.0, 0.0, float(width - 128) / 64.0 - 1.0, 0.0)

# Replace with
		if app.ENABLE_CHATTING_WINDOW_RENEWAL:
			self.imgChatBarLeft.SetPosition(0, 17)
			self.imgChatBarRight.SetPosition(width - 57, 0)

			self.imgChatBarMiddle.SetPosition(57.0, 0)
			self.imgChatBarMiddle.SetRenderingRect(0.0, 0.0, float(width - 57.0 * 2) / 57.0 - 1.0, 0.0)

			self.btnChatTab.SetTextAddPos(uiScriptLocale.CHATTING_SETTING_DEFAULT_TITLE, -2)
			self.btnChatTab.SetPosition(4, 0)
			self.btnChatSettingOption.SetPosition(width - 27, 3)
		else:
			self.imgChatBarLeft.SetPosition(0, 0)
			self.imgChatBarRight.SetPosition(width - 64, 0)
			self.imgChatBarMiddle.SetPosition(64, 0)
			self.imgChatBarMiddle.SetRenderingRect(0.0, 0.0, float(width - 128) / 64.0 - 1.0, 0.0)

''' 10. '''
# Search @ class ChatWindow.OnRender
			grp.RenderBar(self.xBar, self.yBar + (self.heightBar - self.curHeightBar) + 10, self.widthBar, self.curHeightBar)

# Replace with
			if app.ENABLE_CHATTING_WINDOW_RENEWAL:
				grp.RenderBar(self.xBar, self.yBar + (self.heightBar - self.curHeightBar) + self.EDIT_LINE_HIDE_HEIGHT, self.widthBar, self.curHeightBar)
			else:
				grp.RenderBar(self.xBar, self.yBar + (self.heightBar - self.curHeightBar) + 10, self.widthBar, self.curHeightBar)

''' 11. '''
# Search
	def BindInterface(self, interface):
		self.chatInputSet.BindInterface(interface)

# Add below
	if app.ENABLE_CHATTING_WINDOW_RENEWAL:
		def __SettingOptionWndOpen(self):
			if self.wndChatSettingOption:
				if self.wndChatSettingOption.IsShow():
					self.wndChatSettingOption.Close()
				else:
					self.wndChatSettingOption.Open()

		def RefreshChatWindow(self):
			if self.wndChatSettingOption:
				for mode in OPTION_CHECKBOX_MODE.iterkeys():
					enable = self.wndChatSettingOption.GetChatModeSetting(mode)
					if enable:
						chat.EnableChatMode(self.chatID, mode)
					else:
						chat.DisableChatMode(self.chatID, mode)

''' 12. '''
# Search @ class ChatLogWindow.__init__
		chat.SetBoardState(self.chatID, chat.BOARD_STATE_LOG)
		for i in self.CHAT_MODE_INDEX:
			chat.EnableChatMode(self.chatID, i)

# Add below
		if app.ENABLE_CHATTING_WINDOW_RENEWAL:
			chat.EnableChatMode(self.chatID, chat.CHAT_TYPE_EXP_INFO)
			chat.EnableChatMode(self.chatID, chat.CHAT_TYPE_ITEM_INFO)
			chat.EnableChatMode(self.chatID, chat.CHAT_TYPE_MONEY_INFO)

''' 13. '''
# Search @ class ChatLogWindow.ToggleAllChatMode
		self.allChatMode = True

		for i in self.CHAT_MODE_INDEX:
			chat.EnableChatMode(self.chatID, i)

# Add below
		if app.ENABLE_CHATTING_WINDOW_RENEWAL:
			chat.EnableChatMode(self.chatID, chat.CHAT_TYPE_EXP_INFO)
			chat.EnableChatMode(self.chatID, chat.CHAT_TYPE_ITEM_INFO)
			chat.EnableChatMode(self.chatID, chat.CHAT_TYPE_MONEY_INFO)

''' 14. '''
# Search @ class ChatLogWindow.ToggleChatMode
			for i in self.CHAT_MODE_INDEX:
				chat.DisableChatMode(self.chatID, i)
			chat.EnableChatMode(self.chatID, mode)

# Add below
			if app.ENABLE_CHATTING_WINDOW_RENEWAL:
				if mode == chat.CHAT_TYPE_INFO:
					chat.EnableChatMode(self.chatID, chat.CHAT_TYPE_EXP_INFO)
					chat.EnableChatMode(self.chatID, chat.CHAT_TYPE_ITEM_INFO)
					chat.EnableChatMode(self.chatID, chat.CHAT_TYPE_MONEY_INFO)

''' 15. '''
# Search
## ChatModeButton
class ChatModeButton(ui.Window):

# Add above
if app.ENABLE_CHATTING_WINDOW_RENEWAL:
	CHECK_BOX_X_POS = 145

	OPTION_CHECKBOX_TALKING = 1
	OPTION_CHECKBOX_PARTY = 2
	OPTION_CHECKBOX_GUILD = 3
	OPTION_CHECKBOX_SHOUT = 4
	OPTION_CHECKBOX_INFO = 5
	OPTION_CHECKBOX_NOTICE = 6
	OPTION_CHECKBOX_DICE = 7
	OPTION_CHECKBOX_EXP_INFO = 8
	OPTION_CHECKBOX_ITEM_INFO = 9
	OPTION_CHECKBOX_MONEY_INFO = 10

	OPTION_CHECKBOX_MODE = {
		chat.CHAT_TYPE_TALKING : OPTION_CHECKBOX_TALKING,
		chat.CHAT_TYPE_INFO : OPTION_CHECKBOX_INFO,
		chat.CHAT_TYPE_NOTICE : OPTION_CHECKBOX_NOTICE,
		chat.CHAT_TYPE_PARTY : OPTION_CHECKBOX_PARTY,
		chat.CHAT_TYPE_GUILD : OPTION_CHECKBOX_GUILD,
		chat.CHAT_TYPE_SHOUT : OPTION_CHECKBOX_SHOUT,
		chat.CHAT_TYPE_DICE_INFO : OPTION_CHECKBOX_DICE,
		chat.CHAT_TYPE_EXP_INFO : OPTION_CHECKBOX_EXP_INFO,
		chat.CHAT_TYPE_ITEM_INFO : OPTION_CHECKBOX_ITEM_INFO,
		chat.CHAT_TYPE_MONEY_INFO : OPTION_CHECKBOX_MONEY_INFO,
	}

	## ChatSettingWindow
	class ChatSettingWindow(ui.ScriptWindow):
		__author__ = "Owsap"
		__copyright__ = "Copyright 2021, Owsap Productions"

		class MouseReflector(ui.Window):
			def __init__(self, parent):
				ui.Window.__init__(self)
				self.SetParent(parent)
				self.AddFlag("not_pick")
				self.width = self.height = 0
				self.isDown = False

			def __del__(self):
				ui.Window.__del__(self)

			def Down(self):
				self.isDown = True

			def Up(self):
				self.isDown = False

			def OnRender(self):
				if self.isDown:
					grp.SetColor(ui.WHITE_COLOR)
				else:
					grp.SetColor(ui.HALF_WHITE_COLOR)

				x, y = self.GetGlobalPosition()
				grp.RenderBar(x + 2, y + 2, self.GetWidth() - 4, self.GetHeight() - 4)

		class CheckBox(ui.ImageBox):
			def __init__(self, parent, x, y, event, filename = "d:/ymir work/ui/chat/chattingoption_check_box_off.sub"):
				ui.ImageBox.__init__(self)
				self.SetParent(parent)
				self.SetPosition(x, y)
				self.LoadImage(filename)

				self.mouseReflector = parent.MouseReflector(self)
				self.mouseReflector.SetSize(self.GetWidth(), self.GetHeight())

				image = ui.MakeImageBox(self, "d:/ymir work/ui/public/check_image.sub", 0, 0)
				image.AddFlag("not_pick")
				image.SetWindowHorizontalAlignCenter()
				image.SetWindowVerticalAlignCenter()
				image.Hide()

				self.check = False
				self.enable = True
				self.image = image
				self.event = event
				self.Show()

				self.mouseReflector.UpdateRect()

			def __del__(self):
				ui.ImageBox.__del__(self)

			def GetCheck(self):
				return self.check

			def SetCheck(self, flag):
				if flag:
					self.check = True
					self.image.Show()
				else:
					self.check = False
					self.image.Hide()

			def Disable(self):
				self.enable = False

			def OnMouseOverIn(self):
				if not self.enable:
					return
				self.mouseReflector.Show()

			def OnMouseOverOut(self):
				if not self.enable:
					return
				self.mouseReflector.Hide()

			def OnMouseLeftButtonDown(self):
				if not self.enable:
					return
				self.mouseReflector.Down()

			def OnMouseLeftButtonUp(self):
				if not self.enable:
					return
				self.mouseReflector.Up()
				self.event()

		def __init__(self, parent):
			ui.ScriptWindow.__init__(self)
			self.isLoaded = False

			from _weakref import proxy
			self.parent = proxy(parent)
			self.questionDialog = None

			self.checkBoxSlotDict = {}
			self.tmpCheckBoxSettingDict = {}

			self.__LoadWindow()

		def __del__(self):
			ui.ScriptWindow.__del__(self)
			self.isLoaded = False
			self.parent = None
			self.questionDialog = None
			self.checkBoxSlotDict = {}
			self.tmpCheckBoxSettingDict = {}

		def __LoadWindow(self):
			if self.isLoaded:
				return

			self.isLoaded = 1

			try:
				pyScrLoader = ui.PythonScriptLoader()
				pyScrLoader.LoadScriptFile(self, "UIScript/ChatSettingWindow.py")
			except:
				import exception
				exception.Abort("ChatSettingWindow.LoadWindow.LoadScript")

			try:
				self.__BindObject()
			except:
				import exception
				exception.Abort("ChatSettingWindow.LoadWindow.BindObject")

			try:
				self.__CreateObject()
			except:
				import exception
				exception.Abort("ChatSettingWindow.LoadWindow.CreateObject")

			try:
				self.__LoadChattingOptionFile()
			except:
				self.__SaveDefault()

		def __BindObject(self):
			self.GetChild("board").SetCloseEvent(ui.__mem_func__(self.Close))

			self.resetBtn = self.GetChild("reset_button")
			self.resetBtn.SetEvent(ui.__mem_func__(self.__OnClickPopUpSetting), localeInfo.CHATTING_SETTING_CLEAR_QUESTION)

			self.saveBtn = self.GetChild("save_button")
			self.saveBtn.SetEvent(ui.__mem_func__(self.__OnClickSave))

			self.cancelBtn = self.GetChild("cancle_button")
			self.cancelBtn.SetEvent(ui.__mem_func__(self.Close))

		def __CreateObject(self):
			for key in xrange(1, len(OPTION_CHECKBOX_MODE) + 1):
				event = lambda index = key : ui.__mem_func__(self.SetCurrentChatOption)(index)

				# chatting_setting_talking_bg.y + (31 * y)
				yPos = 64 + (31 * 0)
				if key >= OPTION_CHECKBOX_DICE:
					yPos = 64 + (31 * 1)
				if key >= OPTION_CHECKBOX_EXP_INFO:
					yPos = 64 + (31 * 2)

				self.checkBoxSlotDict[key] = self.CheckBox(self, CHECK_BOX_X_POS, yPos + (18 * (key - 1)), event)

		def __OnClickSave(self):
			self.__SaveFile()

			if self.parent:
				self.parent.RefreshChatWindow()

			self.Close()

		def __GetChattingFile(self):
			path = ["UserData", "chatting"]
			try:
				if not os.path.exists(os.getcwd() + os.sep + path[0] + os.sep + path[1]):
					os.makedirs(os.getcwd() + os.sep + "UserData" + os.sep + "chatting")
			except WindowsError as error: pass
			return "%s/%s/%s" % (path[0], path[1], player.GetName())

		def __LoadChattingOptionFile(self):
			load = False
			try:
				fileName = self.__GetChattingFile()
				file = open(fileName)
				try:
					#cPickle.dumps(file)
					load = True
					self.tmpCheckBoxSettingDict = cPickle.load(file)
				except (ValueError, EOFError, cPickle.PicklingError, cPickle.UnpicklingError): pass
			except IOError: pass

			for key in xrange(1, len(OPTION_CHECKBOX_MODE) + 1):
				if not load:
					value = True
					self.tmpCheckBoxSettingDict[key] = True
				else:
					value = self.tmpCheckBoxSettingDict[key]
				self.checkBoxSlotDict[key].SetCheck(value)

			if not load:
				self.__SaveDefault()

		def __SaveFile(self):
			if not self.tmpCheckBoxSettingDict:
				return

			try:
				fileName = self.__GetChattingFile()
				file = open(fileName, 'wb')
				cPickle.dump(self.tmpCheckBoxSettingDict, file)
			except IOError:
				return

		def __SaveDefault(self):
			for key in xrange(1, len(OPTION_CHECKBOX_MODE) + 1):
				self.tmpCheckBoxSettingDict[key] = True

			try:
				fileName = self.__GetChattingFile()
				file = open(fileName, 'wb')
				cPickle.dump(self.tmpCheckBoxSettingDict, file)
			except IOError:
				return

		def __OnClickPopUpSetting(self, text):
			questionDialog = uiCommon.QuestionDialog()
			questionDialog.SetText(text)
			questionDialog.SetAcceptEvent(ui.__mem_func__(self.__QuestionPopupAccept))
			questionDialog.SetCancelEvent(ui.__mem_func__(self.__QuestionPopupCancle))
			questionDialog.Open()
			self.questionDialog = questionDialog

		def __QuestionPopupAccept(self):
			if not self.questionDialog:
				return

			self.__SaveDefault()

			if self.parent:
				self.parent.RefreshChatWindow()

			self.__QuestionPopupCancle()
			self.Close()

		def __QuestionPopupCancle(self):
			self.questionDialog.Close()
			self.questionDialog = None

		def SetCurrentChatOption(self, index):
			value = False
			if not self.checkBoxSlotDict[index].GetCheck():
				value = True

			self.checkBoxSlotDict[index].SetCheck(value)
			self.tmpCheckBoxSettingDict.update({index: value})

		def GetChatModeSetting(self, mode):
			try:
				value = OPTION_CHECKBOX_MODE[mode]
				return self.tmpCheckBoxSettingDict[value]
			except KeyError:
				return True

		def OnPressEscapeKey(self):
			self.Close()
			return True

		def Open(self):
			if not self.isLoaded:
				self.__LoadWindow()

			try:
				self.__LoadChattingOptionFile()
			except:
				self.__SaveDefault()

			self.Show()

		def Close(self):
			if self.questionDialog:
				self.questionDialog.Close()

			self.Hide()