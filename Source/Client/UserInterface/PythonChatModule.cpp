/// 1.
// Search
	PyModule_AddIntConstant(poModule, "CHAT_TYPE_NOTICE", CHAT_TYPE_NOTICE);

// Add below
#if defined(ENABLE_CHATTING_WINDOW_RENEWAL)
	PyModule_AddIntConstant(poModule, "CHAT_TYPE_EXP_INFO", CHAT_TYPE_EXP_INFO);
	PyModule_AddIntConstant(poModule, "CHAT_TYPE_ITEM_INFO", CHAT_TYPE_ITEM_INFO);
	PyModule_AddIntConstant(poModule, "CHAT_TYPE_MONEY_INFO", CHAT_TYPE_MONEY_INFO);
#endif