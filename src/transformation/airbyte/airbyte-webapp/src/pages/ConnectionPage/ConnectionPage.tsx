import React, { Suspense } from "react";
import { Route, Routes } from "react-router-dom";

import { LoadingPage } from "components";

import { ResourceNotFoundErrorBoundary } from "views/common/ResorceNotFoundErrorBoundary";
import { StartOverErrorView } from "views/common/StartOverErrorView";

import { RoutePaths } from "../routePaths";

const CreationFormPage = React.lazy(() => import("./pages/CreationFormPage/CreationFormPage"));
const ConnectionItemPage = React.lazy(() => import("./pages/ConnectionItemPage/ConnectionItemPage"));
const AllConnectionsPage = React.lazy(() => import("./pages/AllConnectionsPage"));

export const ConnectionPage: React.FC = () => (
  <Suspense fallback={<LoadingPage />}>
    <Routes>
      <Route path={RoutePaths.ConnectionNew} element={<CreationFormPage />} />
      <Route
        path=":connectionId/*"
        element={
          <ResourceNotFoundErrorBoundary errorComponent={<StartOverErrorView />}>
            <ConnectionItemPage />
          </ResourceNotFoundErrorBoundary>
        }
      />
      <Route index element={<AllConnectionsPage />} />
    </Routes>
  </Suspense>
);
