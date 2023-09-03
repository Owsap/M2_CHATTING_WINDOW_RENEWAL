/*
* CHAT_TYPE_EXP_INFO :
*	"상자에서 부터 신비한 빛이 나옵니다."
*	"%d의 경험치를 획득했습니다."
*
* CHAT_TYPE_ITEM_INFO :
*	"아이템 획득: %s"
*	"상자에서 %s 가 %d 개 나왔습니다."
*	"상자에서 %s 가 나왔습니다."
*
* CHAT_TYPE_MONEY_INFO :
*	"돈 %d 냥을 획득했습니다."
*/

/// 1.
// Search all
ChatPacket(CHAT_TYPE_INFO, LC_TEXT("돈 %d 냥을 획득했습니다."), dwCounts[i]);

// Replace with
#if defined(__CHATTING_WINDOW_RENEWAL__)
ChatPacket(CHAT_TYPE_MONEY_INFO, LC_TEXT("돈 %d 냥을 획득했습니다."), dwCounts[i]);
#else
ChatPacket(CHAT_TYPE_INFO, LC_TEXT("돈 %d 냥을 획득했습니다."), dwCounts[i]);
#endif

/// 2.
// Search all
ChatPacket(CHAT_TYPE_INFO, LC_TEXT("상자에서 부터 신비한 빛이 나옵니다."));
ChatPacket(CHAT_TYPE_INFO, LC_TEXT("%d의 경험치를 획득했습니다."), dwCounts[i]);

// Replace with
#if defined(__CHATTING_WINDOW_RENEWAL__)
ChatPacket(CHAT_TYPE_EXP_INFO, LC_TEXT("상자에서 부터 신비한 빛이 나옵니다."));
ChatPacket(CHAT_TYPE_EXP_INFO, LC_TEXT("%d의 경험치를 획득했습니다."), dwCounts[i]);
#else
ChatPacket(CHAT_TYPE_INFO, LC_TEXT("상자에서 부터 신비한 빛이 나옵니다."));
ChatPacket(CHAT_TYPE_INFO, LC_TEXT("%d의 경험치를 획득했습니다."), dwCounts[i]);
#endif

/// 3.
// Search all
ChatPacket(CHAT_TYPE_INFO, LC_TEXT("아이템 획득: %s"), item->GetName());

// Replace with
#if defined(__CHATTING_WINDOW_RENEWAL__)
ChatPacket(CHAT_TYPE_ITEM_INFO, LC_TEXT("아이템 획득: %s"), item->GetName());
#else
ChatPacket(CHAT_TYPE_INFO, LC_TEXT("아이템 획득: %s"), item->GetName());
#endif

/// 4.
// Search all
ChatPacket(CHAT_TYPE_INFO, LC_TEXT("아이템 획득: %s"), item2->GetName());

// Replace with
#if defined(__CHATTING_WINDOW_RENEWAL__)
ChatPacket(CHAT_TYPE_ITEM_INFO, LC_TEXT("아이템 획득: %s"), item2->GetName());
#else
ChatPacket(CHAT_TYPE_INFO, LC_TEXT("아이템 획득: %s"), item2->GetName());
#endif

/// 5.
// Search all
if (dwCounts[i] > 1)
	ChatPacket(CHAT_TYPE_INFO, LC_TEXT("상자에서 %s 가 %d 개 나왔습니다."), item_gets[i]->GetName(), dwCounts[i]);
else
	ChatPacket(CHAT_TYPE_INFO, LC_TEXT("상자에서 %s 가 나왔습니다."), item_gets[i]->GetName());

// Replace with
#if defined(__CHATTING_WINDOW_RENEWAL__)
if (dwCounts[i] > 1)
	ChatPacket(CHAT_TYPE_ITEM_INFO, LC_TEXT("상자에서 %s 가 %d 개 나왔습니다."), item_gets[i]->GetName(), dwCounts[i]);
else
	ChatPacket(CHAT_TYPE_ITEM_INFO, LC_TEXT("상자에서 %s 가 나왔습니다."), item_gets[i]->GetName());
#else
if (dwCounts[i] > 1)
	ChatPacket(CHAT_TYPE_INFO, LC_TEXT("상자에서 %s 가 %d 개 나왔습니다."), item_gets[i]->GetName(), dwCounts[i]);
else
	ChatPacket(CHAT_TYPE_INFO, LC_TEXT("상자에서 %s 가 나왔습니다."), item_gets[i]->GetName());
#endif
