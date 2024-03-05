import React from "react";

const Home = () => {
  const h = (Math.floor(Math.random() * 5) + 1);
  return (
    <div>
      <h1>Home</h1>
      <p>On this source i will develop front- and backend to peform my mathematical analysis labs.</p>
      <img src={"/"+h.toString()+"_lab.png"} class={getClassByIndex(h)}/>
    </div>
  );
};

function getClassByIndex(index: number) {
  if (index<=3){
    return "honda_1";
  }
  if(index===4){
    return "honda_2";
  }
  if(index===5){
    return "honda_3";
  }
}
export default Home;