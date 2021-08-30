/*
* CHAT_TYPE_EXP_INFO :
*	"���ڿ��� ���� �ź��� ���� ���ɴϴ�."
*	"%d�� ����ġ�� ȹ���߽��ϴ�."
*
* CHAT_TYPE_ITEM_INFO :
*	"������ ȹ��: %s"
*	"���ڿ��� %s �� %d �� ���Խ��ϴ�."
*	"���ڿ��� %s �� ���Խ��ϴ�."
*
* CHAT_TYPE_MONEY_INFO :
*	"�� %d ���� ȹ���߽��ϴ�."
*/

/// 1.
// Search all
ChatPacket(CHAT_TYPE_INFO, LC_TEXT("�� %d ���� ȹ���߽��ϴ�."), dwCounts[i]);

// Replace with
#if defined(__CHATTING_WINDOW_RENEWAL__)
ChatPacket(CHAT_TYPE_MONEY_INFO, LC_TEXT("�� %d ���� ȹ���߽��ϴ�."), dwCounts[i]);
#else
ChatPacket(CHAT_TYPE_INFO, LC_TEXT("�� %d ���� ȹ���߽��ϴ�."), dwCounts[i]);
#endif

/// 2.
// Search all
ChatPacket(CHAT_TYPE_INFO, LC_TEXT("���ڿ��� ���� �ź��� ���� ���ɴϴ�."));
ChatPacket(CHAT_TYPE_INFO, LC_TEXT("%d�� ����ġ�� ȹ���߽��ϴ�."), dwCounts[i]);

// Replace with
#if defined(__CHATTING_WINDOW_RENEWAL__)
ChatPacket(CHAT_TYPE_EXP_INFO, LC_TEXT("���ڿ��� ���� �ź��� ���� ���ɴϴ�."));
ChatPacket(CHAT_TYPE_EXP_INFO, LC_TEXT("%d�� ����ġ�� ȹ���߽��ϴ�."), dwCounts[i]);
#else
ChatPacket(CHAT_TYPE_INFO, LC_TEXT("���ڿ��� ���� �ź��� ���� ���ɴϴ�."));
ChatPacket(CHAT_TYPE_INFO, LC_TEXT("%d�� ����ġ�� ȹ���߽��ϴ�."), dwCounts[i]);
#endif

/// 3.
// Search all
ChatPacket(CHAT_TYPE_INFO, LC_TEXT("������ ȹ��: %s"), item2->GetName());

// Replace with
#if defined(__CHATTING_WINDOW_RENEWAL__)
ChatPacket(CHAT_TYPE_ITEM_INFO, LC_TEXT("������ ȹ��: %s"), item->GetName());
#else
ChatPacket(CHAT_TYPE_INFO, LC_TEXT("������ ȹ��: %s"), item->GetName());
#endif

/// 4.
// Search all
ChatPacket(CHAT_TYPE_INFO, LC_TEXT("������ ȹ��: %s"), item2->GetName());

// Replace with
#if defined(__CHATTING_WINDOW_RENEWAL__)
ChatPacket(CHAT_TYPE_ITEM_INFO, LC_TEXT("������ ȹ��: %s"), item2->GetName());
#else
ChatPacket(CHAT_TYPE_INFO, LC_TEXT("������ ȹ��: %s"), item2->GetName());
#endif

/// 5.
// Search all
if (dwCounts[i] > 1)
	ChatPacket(CHAT_TYPE_INFO, LC_TEXT("���ڿ��� %s �� %d �� ���Խ��ϴ�."), item_gets[i]->GetName(), dwCounts[i]);
else
	ChatPacket(CHAT_TYPE_INFO, LC_TEXT("���ڿ��� %s �� ���Խ��ϴ�."), item_gets[i]->GetName());

// Replace with
#if defined(__CHATTING_WINDOW_RENEWAL__)
if (dwCounts[i] > 1)
	ChatPacket(CHAT_TYPE_ITEM_INFO, LC_TEXT("���ڿ��� %s �� %d �� ���Խ��ϴ�."), item_gets[i]->GetName(), dwCounts[i]);
else
	ChatPacket(CHAT_TYPE_ITEM_INFO, LC_TEXT("���ڿ��� %s �� ���Խ��ϴ�."), item_gets[i]->GetName());
#else
if (dwCounts[i] > 1)
	ChatPacket(CHAT_TYPE_INFO, LC_TEXT("���ڿ��� %s �� %d �� ���Խ��ϴ�."), item_gets[i]->GetName(), dwCounts[i]);
else
	ChatPacket(CHAT_TYPE_INFO, LC_TEXT("���ڿ��� %s �� ���Խ��ϴ�."), item_gets[i]->GetName());
#endif