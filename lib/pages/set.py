from .productpage import *
from .userpage import *
from .buypage import *
from .vedio import *
from .planttreepages import *
from base.utils import Conf


#用户中心相关Page集合类
class UserPages:
    登录页=LoginPage()
    用户中心=UserCenterPage()
    浏览记录=BrowseRecordPage()
    设置页=SetAppPage()
    收藏页=FavouritePage()

#商品page集合类（商品主干流程相关的）
class ProductPages:
    sale_home_page=HomePage() #特卖首页
    category_list_search_page=CategoryListPage()  #分类列表搜索页
    search_result_list_page=SearchListPage()      #搜索结果页
    商品详情页=ProductDetailsPage()


class BuyPages:
    我的订单页=MyOrderPage()
    结算页=BuySettlementPage()
    支付订单页=PayOrderPage()

class VedioPages:
    视频发布页=VideoReleasePage()

class PlantTreePages:
    plant_tree_home_page=PlantTreeHomePage()
    my_tree_page = MyTreePage()
    other_tree_page = OtherTreePage()


