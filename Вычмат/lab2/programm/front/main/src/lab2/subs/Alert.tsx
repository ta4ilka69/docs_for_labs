import * as React from 'react';
import Alert from '@mui/material/Alert';
import Stack from '@mui/material/Stack';

export function Alerts({message}) {
  return (
    <Stack spacing={2} marginBottom={1}>
      <Alert severity="warning">{message}</Alert>
    </Stack>
  );
}

export function GoodAlerts({message}) {
  return (
    <Stack spacing={2} marginBottom={1}>
      <Alert severity="success">{message}</Alert>
    </Stack>
  );
}