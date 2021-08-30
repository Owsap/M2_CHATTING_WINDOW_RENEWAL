/// 1.
// Search
	PyModule_AddIntConstant(poModule, "CAMERA_STOP", CPythonApplication::CAMERA_STOP);

// Add below
#if defined(ENABLE_CHATTING_WINDOW_RENEWAL)
	PyModule_AddIntConstant(poModule, "ENABLE_CHATTING_WINDOW_RENEWAL", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_CHATTING_WINDOW_RENEWAL", 0);
#endif