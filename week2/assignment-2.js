//Tast1

console.log("=== Task 1 ===");
function func1(name){
    //每個角色的位置
    const characters = {
    "貝吉塔": { x: -4, y: -1, side:true },
    "辛巴": { x: -3, y: 3, side:true },
    "丁滿": { x: -1, y: 4, side:false },
    "悟空": { x: 0, y: 0, side:true },
    "特南克斯": { x: 1, y: -2, side:true },
    "弗利沙": { x: 4, y: -1, side:false }
  };
    //角色間的距離
    let position = characters[name];
    let arr1=[] ; //放名字和距離
    let arr2=[] ; //比大小

    for(let character_name in characters){
        let distance=Math.abs(position["x"]-characters[character_name]["x"])+Math.abs(position["y"]-characters[character_name]["y"]);
        if (distance===0){
            continue;
        }
        if(position["side"]===characters[character_name]["side"]){
            arr1.push({name:character_name, distance:distance});
            arr2.push(distance);
        }else{
            arr1.push({name:character_name, distance:distance+2});
            arr2.push(distance+2);
    }
    }
    //得出最遠與最近
    let farthest = [];
    let nearest = [];
    for(i=0;i<arr1.length;i++){
        if(arr1[i]["distance"]===Math.max(...arr2)){
            farthest.push(arr1[i]["name"]);
        }
    }
    for(i=0;i<arr1.length;i++){
        if(arr1[i]["distance"]===Math.min(...arr2)){
            nearest.push(arr1[i]["name"]);
    }
    }   

    console.log("最遠"+farthest.join("、")+"；最近"+nearest.join("、"))

}

func1("辛巴");
func1("悟空");
func1("弗利沙");
func1("特南克斯");




//Task2

console.log("=== Task 2 ===");
//服務
const services=[
    {"name":"S1", "r":4.5, "c":1000},
    {"name":"S2", "r":3, "c":1200},
    {"name":"S3", "r":3.8, "c":800}
];
//時間
const schedule=[]
for(let i=0;i<24;i++){
    schedule.push({"t":i, "S1":true, "S2":true, "S3":true})
}
//標準
const standard=["r", "c"]

function func2(ss, start, end, criteria){
    //拆字串
    function separation(string) {
        const match = string.match(/^([a-z]+)([<>=]+)([\dA-Za-z.]+)$/);
        const standard = match[1];
        const operator = match[2];
        const value = match[3]; 
        return { standard: standard, operator: operator, value: value }; 
    }
    const requirement=separation(criteria);
    /*
    requirement.standard：前面的單位
    requirement.operator：中間比較符號
    requirement.value：最後數字或名字
    */
    
    //預約時間
    function reservation(services_name){
        if(schedule[start][services_name]&&schedule[end-1][services_name]){     
            for(let i=start;i<end;i++){                     
                schedule[i][services_name]=false
            }
            console.log(services_name);
        }else{
            console.log("sorry");
        }
    }
    
    if(requirement.standard==="name"){         //判斷是不是name=的格式
        reservation(requirement.value)
    }else{
        let n=Number(requirement.value)
        if(requirement.operator==="<="){   // operator是"<="
            if (standard.includes(requirement.standard)) {
                let Max=services
                    .filter(item => item[requirement.standard]<=n)
                    .sort((a,b)=> b[requirement.standard]-a[requirement.standard]);
                    let found=false;
                    for(const services of Max){
                        if(schedule[start][services["name"]]&&schedule[end-1][services["name"]]){
                            reservation(services["name"])
                            found=true;
                            break
                        }
                    }
                    if(!found){
                    console.log("Sorry");
                }
            }
        } else if(requirement.operator===">="){   // operator是">="
            if (standard.includes(requirement.standard)) {
                let Min=services
                    .filter(item => item[requirement.standard]>=n)
                    .sort((a,b)=> a[requirement.standard]-b[requirement.standard]);
                    let found=false;
                    for(const services of Min){
                        if(schedule[start][services["name"]]&&schedule[end-1][services["name"]]){
                            reservation(services["name"])
                            found=true;
                            break
                        }
                    }
                    if(!found){
                    console.log("Sorry");
                }
            }
        }
    }
}

func2(services, 15, 17, "c>=800");
func2(services, 11, 13, "r<=4");
func2(services, 10, 12, "name=S3");
func2(services, 15, 18, "r>=4.5");
func2(services, 16, 18, "r>=4");
func2(services, 13, 17, "name=S1");
func2(services, 8, 9, "c<=1500");





//Task3

console.log("=== Task 3 ===");
function func3(index){
    let x=Math.floor(index/4);
    let y=index%4;
    let z=25+x*-2;
    if(y===1){
        console.log(z-2);
    }else if(y===2){
        console.log(z-5);
    }else if(y===3){
        console.log(z-4);
    }else {
        console.log(z);
    }
}

func3(1);
func3(5);
func3(10);
func3(30);

//Task4

console.log("=== Task 4 ===");
function func4(sp, stat, n){
    const available=stat.slice();
    const carriages=[]
    for(let i=0;i<sp.length;i++){
        let seat=sp[i]
        let able=available[i]
        carriages.push({carriage_number:i, seat:seat, able:able, closest:Math.abs(seat-n)});
    }
    let nearest=[]
    for(let i=0;i<sp.length;i++){
        if(carriages[i]["able"]==='1'){
            continue;
        }
        nearest.push(carriages[i]["closest"])
    }
    let best=[]
    for(let i=0;i<sp.length;i++){
        if(carriages[i]["able"]==='1'){
            continue;
        }else if(carriages[i]["closest"]===Math.min(...nearest)){
        best.push(carriages[i]["carriage_number"])
        }
    }
    console.log(best.join("、"))
}
func4([3, 1, 5, 4, 3, 2], "101000", 2);
func4([1, 0, 5, 1, 3], "10100", 4);
func4([4, 6, 5, 8], "1000", 4);
