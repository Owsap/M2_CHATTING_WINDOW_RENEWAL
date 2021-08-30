/// 1.
// Search @ void CPythonChat::AppendChat
			pChatSet->m_ShowingChatLineList.push_back(pChatLine);

// Add above
#if defined(ENABLE_CHATTING_WINDOW_RENEWAL)
			if (!pChatSet->CheckMode(pChatLine->iType))
				continue;
#endif

/// 2.
// Search @ void CPythonChat::__Initialize
	m_akD3DXClrChat[CHAT_TYPE_INFO] = D3DXCOLOR(1.0f, 0.785f, 0.785f, 1.0f);

// Add below
#if defined(ENABLE_CHATTING_WINDOW_RENEWAL)
	m_akD3DXClrChat[CHAT_TYPE_EXP_INFO] = D3DXCOLOR(1.0f, 0.785f, 0.785f, 1.0f);
	m_akD3DXClrChat[CHAT_TYPE_ITEM_INFO] = D3DXCOLOR(1.0f, 0.785f, 0.785f, 1.0f);
	m_akD3DXClrChat[CHAT_TYPE_MONEY_INFO] = D3DXCOLOR(1.0f, 0.785f, 0.785f, 1.0f);
#endif