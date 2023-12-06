
import './App.css';
import useDocTitle from './Hooks/useDocTitle';
import useSmoothScroll from './Hooks/useSmoothScroll';


function App() {
  const [docTitle, setDocTitle] = useDocTitle( { title: "Start Page"});

  const [refToScroll, smoothScroll] = useSmoothScroll();
  const [topRef, smoothScrollTop] = useSmoothScroll();
  return (
    <div className="App">
      <button onClick={() => setDocTitle("New One!")}>
        Change Title
      </button>

      <button onClick={smoothScroll} ref={topRef}>
        Scroll
        </button>
      <div style={{marginTop:"150vh"}} ref={refToScroll}>
      I am here

      </div>
      <button onClick={smoothScrollTop}> 
      To Top!</button>


     </div>
  );
}

export default App;
