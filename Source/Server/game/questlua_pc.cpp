/// 1.
// Search @ int pc_give_item_from_special_item_group
					ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("�� %d ���� ȹ���߽��ϴ�."), dwCounts[i]);

// Replace with
#if defined(__CHATTING_WINDOW_RENEWAL__)
					ch->ChatPacket(CHAT_TYPE_MONEY_INFO, LC_TEXT("�� %d ���� ȹ���߽��ϴ�."), dwCounts[i]);
#else
					ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("�� %d ���� ȹ���߽��ϴ�."), dwCounts[i]);
#endif

/// 2.
// Search @ int pc_give_item_from_special_item_group
					ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("�������� ���� �ź��� ���� ���ɴϴ�."));
					ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("%d�� ����ġ�� ȹ���߽��ϴ�."), dwCounts[i]);

// Replace with
#if defined(__CHATTING_WINDOW_RENEWAL__)
					ch->ChatPacket(CHAT_TYPE_EXP_INFO, LC_TEXT("�������� ���� �ź��� ���� ���ɴϴ�."));
					ch->ChatPacket(CHAT_TYPE_EXP_INFO, LC_TEXT("%d�� ����ġ�� ȹ���߽��ϴ�."), dwCounts[i]);
#else
					ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("�������� ���� �ź��� ���� ���ɴϴ�."));
					ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("%d�� ����ġ�� ȹ���߽��ϴ�."), dwCounts[i]);
#endif