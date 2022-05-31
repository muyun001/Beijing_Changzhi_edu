import random


def poker():
    huaSe = ['黑桃', '红桃', '方块', '梅花']
    card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    all_cards = ["大王", "小王"]
    for i in huaSe:
        for j in card:
            all_cards.append(i + j)

    while True:
        card_ = random.choice(all_cards)
        all_cards.remove(card_)  # 防止抽到重复的牌
        print(f"恭喜！抽到的牌是：{card_}")

        if "王" not in card_:
            break


if __name__ == '__main__':
    poker()
