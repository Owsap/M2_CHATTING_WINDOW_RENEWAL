/// 1.
// Search @ int pc_give_item_from_special_item_group
					ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("돈 %d 냥을 획득했습니다."), dwCounts[i]);

// Replace with
#if defined(__CHATTING_WINDOW_RENEWAL__)
					ch->ChatPacket(CHAT_TYPE_MONEY_INFO, LC_TEXT("돈 %d 냥을 획득했습니다."), dwCounts[i]);
#else
					ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("돈 %d 냥을 획득했습니다."), dwCounts[i]);
#endif

/// 2.
// Search @ int pc_give_item_from_special_item_group
					ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("나무에서 부터 신비한 빛이 나옵니다."));
					ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("%d의 경험치를 획득했습니다."), dwCounts[i]);

// Replace with
#if defined(__CHATTING_WINDOW_RENEWAL__)
					ch->ChatPacket(CHAT_TYPE_EXP_INFO, LC_TEXT("나무에서 부터 신비한 빛이 나옵니다."));
					ch->ChatPacket(CHAT_TYPE_EXP_INFO, LC_TEXT("%d의 경험치를 획득했습니다."), dwCounts[i]);
#else
					ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("나무에서 부터 신비한 빛이 나옵니다."));
					ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("%d의 경험치를 획득했습니다."), dwCounts[i]);
#endif