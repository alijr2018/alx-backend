// 6-job_processor.js

import kue from 'kue';

const queue = kue.createQueue();

const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;

  sendNotification(phoneNumber, message);

  done();
});

process.on('unhandledRejection', (reason) => {
  console.error(`Unhandled Rejection at: ${reason.stack || reason}`);
  process.exit(1);
});
