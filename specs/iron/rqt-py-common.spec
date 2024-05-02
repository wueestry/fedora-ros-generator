# Meta Package
Name:           ros-iron-rqt-py-common
Version:        1.3.4
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/rqt_py_common
Summary:        Meta package for ros2-iron-rqt_py_common and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rqt_py_common
Requires:       ros2-iron-rqt_py_common-devel

Obsoletes: ros-iron-rqt-py-common < 1.3.4-1

%description
rqt_py_common provides common functionality for rqt plugins written in
Python. Despite no plugin is provided, this package is part of the
rqt_common_plugins repository to keep refactoring generic
functionality from these common plugins into this package as easy as
possible. Functionality included in this package should cover generic
ROS concepts and should not introduce any special dependencies beside
"ros_base".

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.3.4-1
- Update to latest release
