import { useEffect, useState } from 'react';


const SlidingWindow = ({ data }) => {
    const [start_time, setStartTime] = useState(new Date().getTime());
    const [time, setTime] = useState(0); // delta time since start in ms

    setInterval(() => {
        var current_time = new Date().getTime();
        setTime(current_time - start_time);
    }, 10);

    useEffect(() => {
        var slider = document.getElementById("slider" + time);
        var left = Math.sin(time / 1000) * 50 + 50;
        slider.style.left = left + "%";
    }, [time]);


    return (
        <></>
    );
}

export default SlidingWindow;