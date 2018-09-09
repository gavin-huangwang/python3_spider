def china(start,end):
    for page in range(start,end+1):
        yield 'http://tech.china.com/articles/index_'+str(page)+'.html'

#微博start_url生成,uid用户id
def weibo(uid):
    uid_l = [3623353053, 1708288824, 1280981624, 1228196907, 1937439635, 1763362173, ]
    for uid in uid_l:
        #用户详情页url
        user_url='https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&value={uid}&containerid=230283{uid}'
        #关注页url
        followers_url='https://m.weibo.cn/api/container/getIndex?containerid=231051_ - _followers_ - _{uid}&page={page}'
        #粉丝页url
        fans_url='https://m.weibo.cn/api/container/getIndex?containerid=231051_ - _fans_ - _{uid}&page={page}'
        #个人微博页url
        weibo_url='https://m.weibo.cn/api/container/getIndex?uid={uid}&containerid=230413{uid}&type=uid&page={page}'
        yield start_l=[user_url,fans_url,followers_url,weibo_url]

