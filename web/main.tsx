/**
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 *
 */

import React from "react";
import ReactDOM from "react-dom/client";

import App from "./app";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <div className="App">
      <h1>FBKINGDOM-FONT Playground</h1>
      <App />
    </div>
  </React.StrictMode>,
);