from .models import Profile, User, Board, Notice, NoticeComment, BoardComment, Policy, Category_Policy
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.SerializerMethodField('get_username')
    password = serializers.SerializerMethodField('get_password')
    is_staff = serializers.SerializerMethodField('get_is_staff')
    when = serializers.SerializerMethodField('get_when')
    pick_policies = serializers.SerializerMethodField('get_pick_policies')

    class Meta:
        model = Profile
        fields = ('id', 'username', 'password', 'name', 'favorite', 'when', 'is_staff', 'pick_policies')
        
    def get_username(self, obj):
        return obj.user.username

    def get_password(self, obj):
        return obj.user.password

    def get_is_staff(self, obj):
        if obj.user.is_staff:
            return "staff"
        return "user"
    
    def get_when(self, obj):
        print(obj.when)
        return str(obj.when)[0:10]

    def get_pick_policies(self, obj):
        pick_policies = list()
        for item in obj.user.pick_policies.all():
            pick_policies.append(item.id)
        print('profile')
        print(pick_policies)
        return pick_policies

class SessionSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_user')
    name = serializers.SerializerMethodField('get_name')
    favorite = serializers.SerializerMethodField('get_favorite')
    when = serializers.SerializerMethodField('get_when')
    token = serializers.SerializerMethodField('get_token')
    is_authenticated = serializers.SerializerMethodField('get_is_authenticated')
    is_staff = serializers.SerializerMethodField('get_is_staff')
    pick_policies = serializers.SerializerMethodField('get_pick_policies')

    class Meta:
        model = Profile
        fields = ('username', 'name', 'favorite', 'when', 'token', 'is_authenticated', 'is_staff', 'pick_policies')

    def get_user(self, obj):
        return str(obj['username'])

    def get_name(self, obj):
        print(obj['name'])
        return str(obj['name'])

    def get_when(self, obj):
        print(obj['when'])
        return str(obj['when'])

    def get_favorite(self, obj):
        inputFavorite = str(obj['favorite'])
        strFavorite = inputFavorite.replace('\', \'', " ").strip('[\'\']')
        objFavorite = strFavorite.split(" ")
        convertFavorite = {}
        for f in objFavorite:
            if f=='00':
                convertFavorite['00']='등록된 관심 카테고리가 없습니다..'
                break
            elif f=='01':
                convertFavorite['01']='임신/출산'
            elif f=='02':
                convertFavorite['02']='영유아'
            elif f=='03':
                convertFavorite['03']='아동/청소년'
            elif f=='04':
                convertFavorite['04']='청년'
            elif f=='05':
                convertFavorite['05']='중장년'
            elif f=='06':
                convertFavorite['06']='노년'
            elif f=='07':
                convertFavorite['07']='장애인'
            elif f=='08':
                convertFavorite['08']='한부모'
            elif f=='09':
                convertFavorite['09']='다문화(새터민)'
            elif f=='10':
                convertFavorite['10']='저소득층'
            elif f=='11':
                convertFavorite['11']='교육'
            elif f=='12':
                convertFavorite['12']='고용'
            elif f=='13':
                convertFavorite['13']='주거'
            elif f=='14':
                convertFavorite['14']='건강'
            elif f=='15':
                convertFavorite['15']='서민금융'
            elif f=='16':
                convertFavorite['16']='문화'
        return convertFavorite

    def get_token(self, obj):
        print(obj['token'])
        return str(obj['token'])

    def get_is_authenticated(self, obj):
        print(obj['is_authenticated'])
        return obj['is_authenticated']

    def get_is_staff(self, obj):
        print(obj['is_staff'])
        return obj['is_staff']

    def get_pick_policies(self, obj):
        pick_policies = list()
        print(obj)
        if obj.get('pick_policies') != None:
            for item in obj['pick_policies']:
                pick_policies.append(item.id)
            print(pick_policies)
        return pick_policies
        

class UserSerializer(serializers.ModelSerializer):
    genres_array = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')


''' 💓💓💓💓💓 자유게시판 Serializers '''
class BoardSerializer(serializers.ModelSerializer):
    writer = serializers.SerializerMethodField('get_writer')
    email = serializers.SerializerMethodField('get_email')
    when = serializers.SerializerMethodField('get_when')
    comments = serializers.SerializerMethodField('get_comments')

    class Meta:
        model = Board
        fields = ('id', 'when', 'clicked','writer', 'email', 'title', 'content','comments')
    
    def get_writer(self, obj):
        return obj.writer.profile.name
    
    def get_email(self, obj):
        return obj.writer.username 
    
    def get_when(self, obj):
        when =str(obj.when)[:10]
        return when
        
    def get_comments(self, obj):
        print(obj)
        items = BoardComment.objects.filter(post__id=obj.id)
        comments = len(items)
        return comments


class BoardCommentSerializer(serializers.ModelSerializer):
    writer = serializers.SerializerMethodField('get_writer')
    email = serializers.SerializerMethodField('get_email')
    when = serializers.SerializerMethodField('get_when')

    class Meta:
        model = BoardComment
        fields = ('id', 'when','writer', 'email', 'post', 'content', 'edit')

    def get_writer(self, obj):
        return obj.writer.profile.name
    
    def get_email(self, obj):
        return obj.writer.username 

    def get_when(self, obj):
        when =str(obj.when)[:10]
        return when


''' 💓💓💓💓💓 공지사항 Serializers '''
class NoticeSerializer(serializers.ModelSerializer):
    writer = serializers.SerializerMethodField('get_writer')
    is_staff = serializers.SerializerMethodField('get_is_staff')
    when = serializers.SerializerMethodField('get_when')
    email = serializers.SerializerMethodField('get_email')
    comments = serializers.SerializerMethodField('get_comments')

    class Meta:
        model = Notice
        fields = ('id', 'comments','when', 'email', 'clicked', 'writer', 'is_staff', 'title', 'content')

    def get_writer(self, obj):
        return obj.writer.profile.name
    
    def get_is_staff(self, obj):
        return obj.writer.is_staff

    def get_when(self, obj):
        when =str(obj.when)[:10]
        return when

    def get_email(self, obj):
        return obj.writer.username 

    def get_comments(self, obj):
        print(obj)
        items = NoticeComment.objects.filter(post__id=obj.id)
        comments = len(items)
        return comments


class NoticeCommentSerializer(serializers.ModelSerializer):
    writer = serializers.SerializerMethodField('get_writer')
    email = serializers.SerializerMethodField('get_email')
    when = serializers.SerializerMethodField('get_when')

    class Meta:
        model = NoticeComment
        fields = ('id','when', 'writer', 'email', 'post', 'content', 'edit')

    def get_writer(self, obj):
        return obj.writer.profile.name
    
    def get_email(self, obj):
        return obj.writer.username

    def get_when(self, obj):
        when =str(obj.when)[:10]
        return when

class PolicySerializer(serializers.ModelSerializer):
    target = serializers.SerializerMethodField('get_target')
    criteria = serializers.SerializerMethodField('get_criteria')
    content = serializers.SerializerMethodField('get_content')
    supply_way = serializers.SerializerMethodField('get_supply_way')
    procedure = serializers.SerializerMethodField('get_procedure')
    site = serializers.SerializerMethodField('get_site')

    class Meta:
        model = Policy
        fields = ('id', 'title', 'brief', 'target', 'criteria', 'content', 'supply_way', 'procedure', 'site', 'clicked')


    def get_target(self, obj):
        return strSplit(obj.target)
    
    def get_criteria(self, obj):
        return strSplit(obj.criteria)

    def get_content(self, obj):
        return strSplit(obj.content)

    def get_supply_way(self, obj):
        return strSplit(obj.supply_way)

    def get_procedure(self, obj):
        return strSplit(obj.procedure)

    def get_site(self, obj):
        if obj.site is None:
            return None
        return obj.site.split("|")

    

def strSplit(str):
    if str is None:
        return None
    str = str.split("|")
    arr=[]
    for i in range(1, len(str)):
        arr.append({
            'content': str[i],
            'body': []
        })
                
        temp = arr[i-1]['content'].split('&')
        if len(temp)>1 :
            arr[i-1]['content']=temp[0]

            for j in range(1, len(temp)):
                arr[i-1]['body'].append({
                    'content': temp[j],
                    'body': []
                })

                temp1 = arr[i-1]['body'][j-1]['content'].split('@')
                if len(temp1)>1 :
                    arr[i-1]['body'][j-1]['content']=temp1[0]

                    for k in range(1, len(temp1)):
                        arr[i-1]['body'][j-1]['body'].append({
                            'content': temp1[k],
                            'body': []
                        })

                        temp2 = arr[i-1]['body'][j-1]['body'][k-1]['content'].split('+')
                        if len(temp2)>1 :
                            arr[i-1]['body'][j-1]['body'][k-1]['content']=temp2[0]

                            for z in range(1, len(temp1)):
                                arr[i-1]['body'][j-1]['body'][k-1]['body'].append({
                                    'content': temp2[z],
                                    'body': []
                                })
    return arr

class CategoryPolicySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('get_policy_id')
    title = serializers.SerializerMethodField('get_policy_title')
    brief = serializers.SerializerMethodField('get_policy_brief')
    clicked = serializers.SerializerMethodField('get_policy_clicked')

    class Meta:
        model = Category_Policy
        fields = ('id', 'title', 'brief','clicked')
    
    def get_policy_id(self, obj):
        return obj.policy.id

    def get_policy_title(self, obj):
        return obj.policy.title

    def get_policy_brief(self, obj):
        return obj.policy.brief

    def get_policy_clicked(self, obj):
        return obj.policy.clicked


class AllPolicySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Policy
        fields = ('id', 'title', 'brief', 'clicked')

    