import { Box } from '@mui/material';
export const BoxWrapper = ({ children }) => (
  <Box
    sx={{
      bgcolor: 'background.paper',
      boxShadow: 1,
      borderRadius: 2,
      p: 2,
      m: 2,
      minWidth: 300
    }}
  >
    {children}
  </Box>
);
