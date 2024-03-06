// 6-job_creator.js

import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a test notification message',
};

const job = queue.create('push_notification_code', jobData);

job.on('complete', () => {
  console.log('Notification job completed');
  process.exit(0);
});

job.on('failed', () => {
  console.error('Notification job failed');
  process.exit(1);
});

job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  } else {
    console.error(`Error creating job: ${err}`);
    process.exit(1);
  }
});
