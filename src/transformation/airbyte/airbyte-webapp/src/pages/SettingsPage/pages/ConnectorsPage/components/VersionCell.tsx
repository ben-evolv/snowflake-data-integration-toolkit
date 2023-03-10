import { Field, FieldProps, Form, Formik } from "formik";
import React from "react";
import { FormattedMessage, useIntl } from "react-intl";
import styled from "styled-components";

import { Button } from "components/ui/Button";
import { Input } from "components/ui/Input";

import { DEV_IMAGE_TAG } from "core/domain/connector/constants";

import { FormContent } from "./PageComponents";

interface VersionCellProps {
  version: string;
  currentVersion: string;
  id: string;
  onChange: ({ version, id }: { version: string; id: string }) => void;
  feedback?: "success" | string;
  updating: boolean;
}

const VersionInput = styled(Input)`
  max-width: 145px;
  margin-right: 19px;
`;

const InputField = styled.div<{ showNote?: boolean }>`
  display: inline-block;
  position: relative;
  background: ${({ theme }) => theme.whiteColor};

  &:before {
    position: absolute;
    display: ${({ showNote }) => (showNote ? "block" : "none")};
    content: attr(data-before);
    color: ${({ theme }) => theme.greyColor40};
    top: 10px;
    right: 22px;
    z-index: 3;
  }

  &:focus-within:before {
    display: none;
  }
`;

const SuccessMessage = styled.div`
  color: ${({ theme }) => theme.successColor};
  font-size: 12px;
  line-height: 18px;
  position: absolute;
  text-align: right;
  width: 205px;
  left: -208px;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  white-space: break-spaces;
`;

const ErrorMessage = styled(SuccessMessage)`
  color: ${({ theme }) => theme.dangerColor};
  font-size: 11px;
  line-height: 14px;
`;

const VersionCell: React.FC<VersionCellProps> = ({ id, version, onChange, feedback, currentVersion, updating }) => {
  const { formatMessage } = useIntl();

  const renderFeedback = (dirty: boolean, feedback?: string) => {
    if (feedback && !dirty) {
      if (feedback === "success") {
        return (
          <SuccessMessage>
            <FormattedMessage id="form.savedChange" />
          </SuccessMessage>
        );
      }
      return <ErrorMessage>{feedback}</ErrorMessage>;
    }

    return null;
  };

  const isConnectorUpdatable = currentVersion !== version || currentVersion === DEV_IMAGE_TAG;

  return (
    <FormContent>
      <Formik
        initialValues={{
          version,
        }}
        onSubmit={(values) => onChange({ id, version: values.version })}
      >
        {({ isSubmitting, dirty }) => (
          <Form>
            {renderFeedback(dirty, feedback)}
            <Field name="version">
              {({ field }: FieldProps<string>) => (
                <InputField
                  showNote={version === field.value}
                  data-before={formatMessage({
                    id: "admin.latestNote",
                  })}
                >
                  <VersionInput {...field} type="text" autoComplete="off" />
                </InputField>
              )}
            </Field>
            <Button
              size="xs"
              isLoading={isSubmitting || updating}
              type="submit"
              disabled={(isSubmitting || !dirty) && !isConnectorUpdatable}
            >
              <FormattedMessage id="form.change" />
            </Button>
          </Form>
        )}
      </Formik>
    </FormContent>
  );
};

export default VersionCell;
