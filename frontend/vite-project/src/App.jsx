import { useState } from "react";

function App() {
  const [squareFootage, setSquareFootage] = useState("");
  const [predictedPrice, setPredictedPrice] = useState(null);

  const handlePredict = async () => {
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ square_footage: parseFloat(squareFootage) }),
    });

    const data = await response.json();
    setPredictedPrice(data.predicted_price);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>House Price Predictor ( Pathardi Phata Area )</h1>
      <input
        type="number"
        placeholder="Enter square footage"
        value={squareFootage}
        onChange={(e) => setSquareFootage(e.target.value)}
      />
      <button onClick={handlePredict}>Predict Price</button>
      {predictedPrice && <h2>Predicted Price: {predictedPrice}</h2>}
    </div>
  );
}

export default App;
