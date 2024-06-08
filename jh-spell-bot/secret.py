def to_ye_olde_english(text):
    replacements = {
        "you": "thou",
        "your": "thy",
        "you're": "thou art",
        "you are": "thou art",
        "are you": "art thou",
        "have": "hast",
        "hello": "hail",
        "hi": "hail",
        "my": "mine",
        "mine": "myne",
        "i am": "i be",
        "am i": "be i",
        "is": "be",
        "am": "be",
        "was": "wert",
        "were": "wert",
        "do": "dost",
        "does": "doth",
        "will": "wilt",
        "shall": "shalt",
        "would": "wouldst",
        "could": "couldst",
        "should": "shouldst",
        "can": "canst",
        "cannot": "canst not",
        "can't": "canst not",
        "not": "nay",
        "yes": "yea",
        "no": "nay",
        "goodbye": "fare thee well",
        "good bye": "fare thee well",
        "bye": "farewell",
        "thanks": "gramercy",
        "thank you": "gramercy",
        "please": "prithee",
        "excuse me": "prithee pardon",
        "sorry": "forgive me",
        "oops": "o woe",
        "lol": "verily",
        "haha": "verily",
        "oh": "o",
        "hey": "hail",
        "okay": "yea",
        "ok": "yea",
        "alright": "yea",
        "alrighty": "yea",
        "really": "verily",
        "sure": "yea",
        "of course": "yea",
        "why": "wherefore",
        "what": "what ho",
        "who": "who art",
        "whom": "whomst",
        "whomst": "whom",
        "whose": "whose",
        "where": "wherefore",
        "when": "whenst",
        "whenst": "when",
        "how": "how now",
        "much": "mickle",
        "very": "right",
        "yes": "yea",
        "indeed": "verily",
        "definitely": "yea",
        "certainly": "yea",
        "absolutely": "yea",
        "totally": "yea",
        "quite": "right",
        "great": "grand",
        "awesome": "wondrous",
        "amazing": "wondrous",
        "cool": "nifty",
        "interesting": "wondrous",
        "fun": "mirthful",
        "fantastic": "wondrous",
        "wonderful": "wondrous",
        "excellent": "noble",
        "brilliant": "noble",
        "beautiful": "fair",
        "nice": "kind",
        "good": "well",
        "bad": "ill",
        "sad": "woeful",
        "happy": "merry",
        "scared": "afeared",
        "afraid": "afeared",
        "angry": "wroth",
        "hungry": "hungerly",
        "thirsty": "thirstly",
        "tired": "weary",
        "sleepy": "drowsy",
        "sick": "ail",
        "ill": "ail",
        "busy": "swink",
        "work": "swink",
        "job": "craft",
        "money": "gold",
        "friend": "comrade",
        "friends": "comrades",
        "enemy": "foe",
        "enemies": "foes",
        "love": "lief",
        "hate": "abhor",
        "like": "fain",
        "dislike": "disfain",
        "want": "wish",
        "need": "must needs",
        "hello": "hail",
        "hi": "hail",
        "bye": "farewell",
        "yes": "yea",
        "no": "nay",
        "goodbye": "fare thee well",
        "thanks": "gramercy",
        "thank you": "gramercy",
        "please": "prithee",
        "excuse me": "prithee pardon",
        "sorry": "forgive me",
        "oops": "o woe",
        "lol": "verily",
        "haha": "verily",
        "oh": "o",
        "hey": "hail",
        "okay": "yea",
    }

    # Replace words in the text using the mapping
    for word, replacement in replacements.items():
        text = text.replace(word, replacement)

    return text