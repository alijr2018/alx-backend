// 7-job_processor.js

import kue from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0);

  if (blacklistedNumbers.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    job.progress(50);

    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    setTimeout(() => {
      job.progress(100);

      done();
    }, 1000);
  }
};

const queue = kue.createQueue({ concurrency: 2 });

queue.process('push_notification_code_2', (job, done) => {
  const { phoneNumber, message } = job.data;

  sendNotification(phoneNumber, message, job, done);
});

process.on('unhandledRejection', (reason) => {
  console.error(`Unhandled Rejection at: ${reason.stack || reason}`);
  process.exit(1);
});
