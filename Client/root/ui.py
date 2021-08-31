''' 1. '''
# Search @ class Button
	def SetText(self, text, height = 4):

# Add above
	def SetTextAddPos(self, text, x_add = 0, y_add = 0, height = 4):
		if not self.ButtonText:
			textLine = TextLine()
			textLine.SetParent(self)
			textLine.SetPosition(self.GetWidth() / 2 + x_add, self.GetHeight() / 2 + y_add)
			textLine.SetVerticalAlignCenter()
			textLine.SetHorizontalAlignCenter()
			textLine.Show()
			self.ButtonText = textLine
		self.ButtonText.SetText(text)