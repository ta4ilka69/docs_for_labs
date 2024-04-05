import React from "react";

const Home = () => {
  const h = Math.floor(Math.random() * 6) + 1;
  return (
    <div>
      <h1>Home</h1>
      <div
        className="flex row fullwidth"
        style={{ justifyContent: "space-around" }}
      >
        <iframe
          width="500"
          height="400"
          src="https://www.myinstants.com/instant/goyda-98284/embed/"
        ></iframe>
      </div>
      <p>
        On this source i will develop front- and backend to peform my
        mathematical analysis labs.
      </p>
      <img src={"/" + h.toString() + "_lab.png"} class={getClassByIndex(h)} />
    </div>
  );
};

function getClassByIndex(index: number) {
  if (index <= 3 || index === 6) {
    return "honda_1";
  }
  if (index === 4) {
    return "honda_2";
  }
  if (index === 5) {
    return "honda_3";
  }
}
export default Home;
