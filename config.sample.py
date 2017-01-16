config = {
    'allow_reply': True,
    'reply_pattern': '^re\s*#(?P<id>\d+)\s+(?P<reply>.*?)$',  # 匹配形如「re#123 你好啊」的消息
    'reply_format': '{{ reply }}\n\n——来自这个世界外的回复',

    'src': [
        {
            'via': 'wx',
            'account': 'your_wechat_id',
            'src_displayname': '微信',
            'api_url': 'http://127.0.0.1:5001/openwx',
            'rules': []
        },
        {
            'via': 'qq',
            'account': '12345678',
            'src_displayname': 'QQ小号',
            'api_url': 'http://127.0.0.1:5000/openqq',
            'rules': [
                {
                    'type': ['group', 'discuss'],
                    'keywords': ['通知', '公告']
                },
                {
                    'type': 'friend',
                    '!sender': '来借钱的'
                }
            ]
        }
    ],
    'dst': [
        {
            'via': 'qq',
            'api_url': 'http://127.0.0.1:5000/openqq',
            'rules': [
                {
                    'type': 'friend',
                    'friend_account': '87654321'
                }
            ]
        }
    ]
}
