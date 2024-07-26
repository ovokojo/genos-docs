import 'package:intl/intl.dart';

String formatDate(DateTime date) {
  return DateFormat('MM-dd-yyyy').format(date);
}

String formatDateLong(DateTime date) {
  return DateFormat('MMMM dd, yyyy').format(date);
}

String formatDateWithTime(DateTime date) {
  return DateFormat('MM-dd-yyyy HH:mm').format(date);
}
