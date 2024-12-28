from sympy.codegen.ast import continue_

from Tool import click_position_record
from Tool import auto_click
from Tool import locate_image
import Click_position_obtain
import AutoClick
import pyautogui
import time
from pynput import mouse
import numpy as np
from Tool import *



def tongshuai():
    # def on_click(x, y, button, pressed):
    #     if button == mouse.Button.right and pressed:
    #         print("Right mouse button clicked. Exiting...")
    #         listener.stop()

    location_tongshuai = locate_image(r'Figures\tongshuai.png', 0.80)
    try:
        x, y = position_cal(location_tongshuai)
        x = x + (1745-1471)
        y = y + (166-156)
        pyautogui.click(x, y)
        print(f"已进入统帅页面")
        time.sleep(2)
        pyautogui.click(x+85, y+132)
        print(f"已领取美如统帅点数，位置在({x}, {y})")
        time.sleep(2)
        pyautogui.click(x + 60, y + 465)
        print(f"已点击每日礼包")
        time.sleep(1)
        pyautogui.click(x + 60, y + 465)
        time.sleep(1)
        pyautogui.click(x + (1465-1745), y + (149-166))
        print(f"已点击返回")
    except:
        print('Find failed.')
    location_tongshuai = locate_image(r'Figures\tongshuai.png', 0.80)
    if location_tongshuai == None:
        print('前面动作有错误，请检查！')
        while 1:
            i = 1

def daily_donate():
    location_lianmeng = locate_image(r'Figures\lianmeng.png', 0.80)
    locate_error_report(location_lianmeng, error_explain='找不到联盟按钮')
    x, y = position_cal(location_lianmeng)
    pyautogui.click(x, y)
    print(f"已进入联盟页面")
    time.sleep(2)
    pyautogui.click(x + (1713 - 1776), y + (714 - 889))
    print(f"已进入联盟科技页面")
    time.sleep(2)
    location_lianmengyongxu = locate_image(r'Figures\lianmengyongxu.png', 0.95)
    if location_lianmengyongxu == None:
        print('前面动作有错误，请检查！')
        while 1:
            i = 1
    x, y = position_cal(location_lianmengyongxu)
    # print(x, y)
    pyautogui.click(x, y)
    print(f"已点击联盟永续")
    time.sleep(2)
    for times in range(25):
        pyautogui.click(x + 55, y)
        time.sleep(0.2)
        print(f"已捐献{times + 1}次")
    pyautogui.click(x + (1465 - 1678), y + (150 - 776))
    time.sleep(2)
    pyautogui.click(x + (1465 - 1678), y + (150 - 776))
    time.sleep(2)
    pyautogui.click(x + (1465 - 1678), y + (150 - 776))
    time.sleep(2)
    location_tongshuai = locate_image(r'Figures\tongshuai.png', 0.80)
    locate_error_report(location_tongshuai, '前面动作有错误，请检查！')

def beat_monster(location, x_0, y_0):
    # flag = 11
    # while flag>1:
    #     x, y = position_cal(location)
    #     pyautogui.click(x, y)
    #     flag = flag - 1
    #     time.sleep(1)
        # verify enter the next page
        # location_huojing = locate_image(r'Figures\huojing.png', 0.80)
        # if location_huojing != None:
        #     flag = 0
    # if flag==1:
    #     print('点击野怪出错')
    #     exit()

    x, y = position_cal(location)
    pyautogui.click(x, y)

    time.sleep(1)
    location_qianwangchakan = locate_image(r'Figures\qianwangchakan.png', 0.6)
    if location_qianwangchakan != None:
        x, y = position_cal(location_qianwangchakan)
        pyautogui.click(x, y - 15)
        time.sleep(2)
    else:
        print('找不到 前往查看 的点击位置')
        exit()

    location_chuzheng = locate_image(r'Figures\chuzheng.png', 0.80)
    if location_chuzheng != None:
        x, y = position_cal(location_chuzheng)
        pyautogui.click(x, y)
        time.sleep(2)
    else:
        print('找不到出征')
        exit()

    location_jinabiandui = locate_image(r'Figures\biandui6.png', 0.80)
    if location_jinabiandui != None:
        x, y = position_cal(location_jinabiandui)
        pyautogui.click(x, y)
        time.sleep(2)
    else:
        print('找不到编队')
        exit()
    location_jinachuzheng = locate_image(r'Figures\jinachuzheng.png', 0.80)
    if location_jinachuzheng != None:
        x, y = position_cal(location_jinachuzheng)
        pyautogui.click(x, y)
        time.sleep(2)
    else:
        print('找不到出征')
        exit()
    print('打野怪中')
    time.sleep(80)
    location_qingbao = locate_image(r'Figures\qingbao.png', 0.80)
    if location_qingbao != None:
        x, y = position_cal(location_qingbao)
        pyautogui.click(x, y)
        time.sleep(5)
        print('进入情报界面')
    else:
        print('进入情报界面时出错')
        while 1:
            i = 1
    x, y = position_cal(location)
    pyautogui.click(x, y)
    time.sleep(2)
    print('领取奖励')
    pyautogui.click(x_0+50, y_0-100)
    time.sleep(2)

def save_survivor(location):
    flag = 11
    while flag > 1:
        x, y = position_cal(location)
        pyautogui.click(x, y)
        flag = flag - 1
        time.sleep(1)
        # verify enter the next page
        location_tent = locate_image(r'Figures\tent.png', 0.80)
        if location_tent != None:
            flag = 0
    if flag == 1:
        print('点击帐篷出错')
        exit()
    time.sleep(1)
    location_qianwangchakan = locate_image(r'Figures\qianwangchakan.png', 0.6)
    if location_qianwangchakan != None:
        x, y = position_cal(location_qianwangchakan)
        pyautogui.click(x, y - 15)
        time.sleep(2)
    else:
        print('找不到 前往查看 的点击位置')
        exit()

    # pyautogui.click(x_0 + 230, y_0 - 240) # 前往查看
    # time.sleep(2)
    # pyautogui.click(x_0 + 230, y_0 - 400)  # 出征
    # time.sleep(2)
    # pyautogui.click(x_0 + 125, y_0 - 720)  # 选吉娜编队
    # time.sleep(2)
    # pyautogui.click(x_0 + 270, y_0 - 130)  # 选吉娜编队
    # time.sleep(2)
    location_yingjiu = locate_image(r'Figures\yingjiu.png', 0.80)
    if location_yingjiu != None:
        x, y = position_cal(location_yingjiu)
        pyautogui.click(x, y)
        time.sleep(20)
    else:
        print('找不到营救')
        exit()
    enter_intelligence_page()
    x, y = position_cal(location)
    pyautogui.click(x, y)
    time.sleep(2)
    print('领取奖励')
    pyautogui.click(x, y)
    time.sleep(2)

def travel(location):
    flag = 11
    while flag > 1:
        x, y = position_cal(location)
        pyautogui.click(x, y)
        flag = flag - 1
        time.sleep(1)
        # verify enter the next page
        location_yingxiongzhilv = locate_image(r'Figures\yingxiongzhilv.png', 0.80)
        if location_yingxiongzhilv != None:
            flag = 0
    if flag == 1:
        print('点击英雄之旅出错')
        exit()
    time.sleep(1)
    location_qianwangchakan = locate_image(r'Figures\qianwangchakan.png', 0.7)
    if location_qianwangchakan != None:
        x, y = position_cal(location_qianwangchakan)
        pyautogui.click(x, y - 15)
        time.sleep(2)
    else:
        print('找不到 前往查看 的点击位置')
        exit()
    location_tanxian = locate_image(r'Figures\tanxian.png', 0.80)
    if location_tanxian != None:
        x, y = position_cal(location_tanxian)
        pyautogui.click(x, y)
        time.sleep(2)
    else:
        print('找不到探险')
        exit()
    location_zhandou = locate_image(r'Figures\zhandou.png', 0.80)
    if location_zhandou != None:
        x, y = position_cal(location_zhandou)
        pyautogui.click(x, y)
        time.sleep(2)
    else:
        print('找不到战斗')
        exit()
    flag = 60 # 计时60秒
    while flag > 1:
        location_shengli = locate_image(r'Figures\shengli.png', 0.80)
        if location_shengli != None:
            x, y = position_cal(location_zhandou) # 退出胜利结算页面
            pyautogui.click(x, y)
            time.sleep(2)
            flag = 0
        else:
            flag = flag - 1
            time.sleep(1)
    if flag == 1:
        print('战斗失败，请查看原因')
        exit()
    enter_intelligence_page() #返回情报界面

    x, y = position_cal(location)
    pyautogui.click(x, y)
    time.sleep(2)
    print('领取奖励')
    location_jiangli = locate_image(r'Figures/reward.png', 0.80)
    if location_jiangli != None:
        x, y = position_cal(location_jiangli)
    pyautogui.click(x, y)
    time.sleep(2)

def intelligence():
    location_chengzheng = locate_image(r'Figures\chengzhen.png', 0.80)
    flag = 0  # 进入情报直到回到野外界面
    if location_chengzheng == None:
        print('目前不在野外界面')
        location_yewai = locate_image(r'Figures\field.png', 0.80)
        if location_yewai != None:
            left_click(location_yewai, 1)
        while flag == 0:
            location_chengzheng = locate_image(r'Figures\chengzhen.png', 0.80)
            if location_chengzheng != None:
                flag = 1
            time.sleep(random_time(1))
    enter_field_page() # 进入野外界面
    (x_0, y_0) = enter_intelligence_page() # 进入情报界面，并返回游戏界面左下角坐标

    flag = 6 # 情报的种类数量
    while flag != 0:
        flag = 6
        location_goldmonster = locate_image(r'Figures\golden monster.png', 0.80)
        if location_goldmonster==None:
            location_goldmonster = locate_image(r'Figures\golden monster2.png', 0.80)
        if location_goldmonster == None:
            flag = flag - 1
            print('No golden monster')
        else:
            print('Go to beat golden monster')
            beat_monster(location_goldmonster, x_0, y_0)

        location_purplemonster = locate_image(r'Figures\purplemonster.png', 0.80)
        if location_purplemonster == None:
            location_purplemonster = locate_image(r'Figures\purplemonster2.png', 0.80)
        if location_purplemonster == None:
            flag = flag - 1
            print('No purple monster')
        else:
            print('Go to beat purple monster')
            beat_monster(location_purplemonster, x_0, y_0)

        location_bluemonster = locate_image(r'Figures\bluemonster.png', 0.80)
        if location_bluemonster == None:
            location_bluemonster = locate_image(r'Figures\bluemonster2.png', 0.80)
        if location_bluemonster == None:
            flag = flag - 1
            print('No blue monster')
        else:
            print('Go to beat blue monster')
            beat_monster(location_bluemonster, x_0, y_0)
        location_goldtent = locate_image(r'Figures\goldentent.png', 0.80)
        if location_goldtent == None:
            flag = flag - 1
            print('No gold tent')
        else:
            save_survivor(location_goldtent)
        location_purplemtent = locate_image(r'Figures\purpletent.png', 0.80)
        if location_purplemtent == None:
            flag = flag - 1
            print('No purple tent')
        else:
            save_survivor(location_purplemtent)
        # location_bluetent = locate_image(r'Figures\bluetent.png', 0.80)
        # if location_bluetent == None:
        #     flag = flag - 1
        #     print('No purple tent')
        # else:
        #     save_survivor(location_bluetent)
        location_bluetravel = locate_image(r'Figures\blue_travel.png', 0.80)
        if location_bluetravel == None:
            flag = flag - 1
            print('No blue travel')
        else:
            travel(location_bluetravel)
        location_purpletravel = locate_image(r'Figures\purpletravel.png', 0.60)
        if location_purpletravel == None:
            flag = flag - 1
            print('No purple travel')
        else:
            travel(location_purpletravel)
        location_goldentravel = locate_image(r'Figures\goldentravel.png', 0.80)
        if location_goldentravel == None:
            flag = flag - 1
            print('No gold travel')
        else:
            travel(location_goldentravel)
    print('情报任务已完成')
    location_fanhui = locate_image(r'Figures\fanhui.png', 0.80)
    x, y = position_cal(location_fanhui)
    pyautogui.click(x, y)

def xunbao(location):
    x, y = position_cal(location)
    pyautogui.click(x, y)
    time.sleep(2)
    location_xunbaopaiqian = locate_image(r'Figures\xunbaopaiqian.png', 0.80)
    x, y = position_cal(location_xunbaopaiqian)
    pyautogui.click(x, y)
    time.sleep(2)
    location_kaishixunbao = locate_image(r'Figures\kaishixunbao.png', 0.80)
    x, y = position_cal(location_kaishixunbao)
    pyautogui.click(x, y)
    time.sleep(2)
    pyautogui.click(x, y + 110)
    time.sleep(2)

def pet():
    if page_judge()==2:
        print('请返回城镇界面或野外界面')
    # 进入宠物界面
    pet_location = locate_image(r'Figures\pet.png', 0.80)
    locate_error_report(pet_location, '找不到宠物界面入口')
    x, y = position_cal(pet_location)
    pyautogui.click(x, y)
    time.sleep(2)
    location_petfamily = locate_image(r'Figures\petfamily.png', 0.80)
    locate_error_report(location_petfamily, '找不到宠物界面入口')
    x, y = position_cal(location_petfamily)
    pyautogui.click(x, y)
    time.sleep(2)
    print('进入宠物界面')
    # 领悟联盟宝藏
    try:
        location_xunbao = locate_image(r'Figures\xunbao.png', 0.80)
        locate_error_report(location_xunbao, '找不到寻宝界面入口')
        x, y = position_cal(location_xunbao)
        pyautogui.click(x, y)
        time.sleep(2)
        location_lianmengbaozang = locate_image(r'Figures\lianmengbaozang.png', 0.80)
        locate_error_report(location_lianmengbaozang, '找不到联盟宝藏界面入口')
        x, y = position_cal(location_lianmengbaozang)
        pyautogui.click(x, y)
        time.sleep(2)
        location_yijianlingqu = locate_image(r'Figures\yijianlingqu.png', 0.80)
        x, y = position_cal(location_yijianlingqu)
        pyautogui.click(x, y)
        time.sleep(2)
        pyautogui.click(x, y) # 退出领取界面
        time.sleep(2)
        location_cha = locate_image(r'Figures\cha.png', 0.80)
        x, y = position_cal(location_cha)
        pyautogui.click(x, y)
        time.sleep(2)
        print('成功领取联盟宝藏')
    except:
        print('联盟宝藏已领取')
        location_cha = locate_image(r'Figures\cha.png', 0.80)
        x, y = position_cal(location_cha)
        pyautogui.click(x, y)
        time.sleep(2)

    # 领取宝藏任务
    flag = 2
    while flag:
        location_bluebaozang = locate_image(r'Figures\bluebaozang.png', 0.9)
        if location_bluebaozang == None:
            print('没有蓝色宝藏了')
            flag = flag - 1
        else:
            xunbao(location_bluebaozang)
        location_purplebaozang = locate_image(r'Figures\purplebaozang.png', 0.9)
        if location_purplebaozang == None:
            print('没有紫色宝藏')
            flag = flag - 1
        else:
            xunbao(location_purplebaozang)

    location_fanhui = locate_image(r'Figures\fanhui2.png', 0.9)
    x, y = position_cal(location_fanhui)
    pyautogui.click(x, y)
    time.sleep(2)
    pyautogui.click(x, y)
    time.sleep(2)


def auto_beat_monster():
    '''
    自动刷野怪，保证吉娜上阵
    bug: 体力不足，没有队列，野怪等级
    :return:
    '''
    location_chengzheng = locate_image(r'Figures\chengzhen.png', 0.80)
    flag = 0 # 进入自动打怪直到回到野外界面
    if location_chengzheng == None:
        print('目前不在野外界面')
        while flag==0:
            location_yewai = locate_image(r'Figures\field.png', 0.80)
            if location_yewai != None:
                left_click(location_yewai, 1)

            location_chengzheng = locate_image(r'Figures\chengzhen.png', 0.80)
            if location_chengzheng != None:
                flag = 1
            time.sleep(random_time(1))

    location_search = locate_image(r'Figures\search.png', 0.60)
    locate_error_report(location_search, '找不到查找按钮')
    left_click(location_search, 1)

    location_yeshou = locate_image(r'Figures\yeshou.png', 0.80)
    locate_error_report(location_yeshou,'找不到野兽')
    left_click(location_yeshou, 1)

    location_sousuo = locate_image(r'Figures\sousuo.png', 0.80)
    locate_error_report(location_sousuo, '找不到搜索按钮')
    left_click(location_sousuo, 1)

    location_gongji = locate_image(r'Figures\gongji.png', 0.60)
    locate_error_report(location_gongji,'找不到攻击按钮')
    left_click(location_gongji, 1)

    location_biandui6 = locate_image(r'Figures\biandui6.png', 0.80)
    locate_error_report(location_biandui6, "找不到编队6")
    left_click(location_biandui6, 1)

    flag = 1 # 吉娜是否已经回来
    while flag:
        location_jina = locate_image(r'Figures\jina.png', 0.80)
        if location_jina == None:
            left_click(location_biandui6, 4)
        else:
            flag = 0
    location_jinachuzheng = locate_image(r'Figures\jinachuzheng.png', 0.80)
    locate_error_report(location_jinachuzheng, '找不到8体力的出征')
    left_click(location_jinachuzheng, 1)
    print('打野怪中')

def goingout():
    location = locate_image(r'Figures\chuzheng.png', 0.80)
    if location==None:
        location = locate_image(r'Figures\chuzheng_orangebackground_10.png', 0.80)
    locate_error_report(location, '没找到出征按钮')
    left_click(location, 1)

def collecting(location):
    '''

    :param location:
    :return find_or_not, queue_full_or_not:
        find_or_not: 是否找到矿，找到返回1，没招到返回0;
        queue_full_or_not: 是否还有队列，有队列返回1，没有队列返回0
    '''
    find_or_not, queue_full_or_not = 1, 1

    left_click(location, 1)
    location_sousuo = locate_image(r'Figures\sousuo.png', 0.80)
    locate_error_report(location_sousuo, '没找到搜索按钮')
    left_click(location_sousuo, 1)

    # 采集
    location_collecting = locate_image(r'Figures/collect.png', 0.80)
    if location_collecting == None:
        find_or_not = 0 # 没找到矿
    else:
        # 点击采集并出征
        left_click(location_collecting, 1)
        location = locate_image(r'Figures\chuzheng.png', 0.80)
        if location == None:
            location = locate_image(r'Figures\chuzheng_orangebackground_10.png', 0.80)
        if location == None:
            queue_full_or_not = 0
        else:
            left_click(location, 1) # 点击出征
            # 从野外返回搜索界面
            location_search = locate_image(r'Figures\search.png', 0.60)
            locate_error_report(location_search, '找不到查找按钮')
            left_click(location_search, 1)

    if find_or_not==0:
        print('没找到矿')
    if queue_full_or_not==0:
        print('没队列了')
    return find_or_not-1, queue_full_or_not


def auto_collect():
    '''
    自动采集
    bug: 没有队列，矿的等级
    :return:
    '''
    location_chengzheng = locate_image(r'Figures\chengzhen.png', 0.80)
    flag = 0 # 进入自动采集直到回到野外界面
    if location_chengzheng == None:
        print('目前不在野外界面')
        location_yewai = locate_image(r'Figures\field.png', 0.80)
        if location_yewai != None:
            left_click(location_yewai, 1)

        while flag==0:
            location_chengzheng = locate_image(r'Figures\chengzhen.png', 0.80)
            if location_chengzheng != None:
                flag = 1
            time.sleep(random_time(1))

    # 开启牛技能
    cow_skill = 0
    pet_location = locate_image(r'Figures\pet.png', 0.80)
    locate_error_report(pet_location, '找不到宠物界面入口')
    left_click(pet_location, 1)

    location_cow = locate_image(r'Figures\cow.png', 0.80)
    if location_cow != None:
        left_click(location_cow, 1) # 点击牛牛

        location_use = locate_image(r'Figures\use.png', 0.80)
        locate_error_report(location_use, '找不到使用按钮')
        left_click(location_use, 1) # 点击使用

        cow_skill = 1

    location_cha = locate_image(r'Figures\cha.png', 0.80)
    left_click(location_cha, 1)

    location_search = locate_image(r'Figures\search.png', 0.60)
    locate_error_report(location_search, '找不到查找按钮')
    left_click(location_search, 1)

    # 横拉search界面，拉到四种资源都出现
    location_ironore = locate_image(r'Figures\resource_ironore.png', 0.80)
    if location_ironore == None:
        location_meat = locate_image(r'Figures\resource_meat.png', 0.80)
        locate_error_report(location_meat, '找不到生肉')
        x, y = position_cal(location_meat)
        # 拖动资源界面
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown()
        pyautogui.moveTo(x-200, y, duration=1)
        pyautogui.mouseUp()

    queue_full_or_not = 1
    find_or_not = 4
    while queue_full_or_not and find_or_not:
        find_or_not = 4
        # collecting meat
        location_meat = locate_image(r'Figures\resource_meat.png', 0.80)
        if location_meat == None:
            print('没找到生肉按钮')
        else:
            addition, queue_full_or_not = collecting(location_meat)
            find_or_not += addition

        # collecting wood
        location_wood = locate_image(r'Figures\resource_wood.png', 0.50)
        if location_wood == None:
            print('没找到木材按钮')
            exit()
        else:
            addition, queue_full_or_not = collecting(location_wood)
            find_or_not += addition

        # 横拉search界面，拉到四种资源都出现
        location_ironore = locate_image(r'Figures\resource_ironore.png', 0.80)
        if location_ironore == None:
            location_meat = locate_image(r'Figures\resource_meat.png', 0.80)
            locate_error_report(location_meat, '找不到生肉')
            x, y = position_cal(location_meat)
            # 拖动资源界面
            pyautogui.moveTo(x, y)
            pyautogui.mouseDown()
            pyautogui.moveTo(x - 200, y, duration=1)
            pyautogui.mouseUp()

        # collect coal mine
        location_coalmine = locate_image(r'Figures\resource_coalmine.png', 0.80)
        if location_coalmine == None:
            print('没找到煤矿按钮')
            exit()
        else:

            addition, queue_full_or_not = collecting(location_coalmine)
            find_or_not += addition
        # collecting iron ore
        location_ironore = locate_image(r'Figures\resource_ironore.png', 0.80)
        if location_ironore == None:
            print('没找到铁矿按钮')
            exit()
        else:
            addition, queue_full_or_not = collecting(location_ironore)
            find_or_not += addition
        if cow_skill == 0:
            time.sleep(random_time(600))

def adventure():
    if page_judge() == 2:
        exit()
    location_adventure = locate_image(r'Figures\adventure.png', 0.80)
    locate_error_report(location_adventure, '找不到探险按钮')
    left_click(location_adventure, 1)

    location_receive = locate_image(r'Figures\receive.png', 0.80)
    locate_error_report(location_receive, '找不到领取1按钮')
    left_click(location_receive, 1)

    location_receive = locate_image(r'Figures\receive2.png', 0.80)
    if location_receive==None:
        print('探险奖励已领取')
        location_return = locate_image(r'Figures\fanhui2.png', 0.80)
        locate_error_report(location_return, '没找到返回按钮')
        left_click(location_return, 1)
        return 0

    locate_error_report(location_receive, '找不到领取2按钮')
    left_click(location_receive, 1)

    location_reward = locate_image(r'Figures\reward.png', 0.80)
    locate_error_report(location_reward, '没找到奖励')
    left_click(location_reward, 1)

    location_return = locate_image(r'Figures\fanhui2.png', 0.80)
    locate_error_report(location_return, '没找到返回按钮')
    left_click(location_return, 1)

    print('探险奖励已领取')


if __name__ == '__main__':
    daily_donate()
    tongshuai()
    # intelligence()

    # auto_collect()
    # pet()
    # times = int(140/8)
    # while times:
    #     auto_beat_monster()
    #     time.sleep(10)
    #     times = times - 1
    # while 1:
    #     daily_donate()
    #     time.sleep(16*4*20)
    # adventure()
    # auto_collect()