# Meta Package
Name:           ros-humble-rqt-bag
Version:        1.1.4
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_bag
Summary:        Meta package for ros2-humble-rqt_bag and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rqt_bag
Requires:       ros2-humble-rqt_bag-devel

Obsoletes: ros-humble-rqt-bag < 1.1.4-1

%description
rqt_bag provides a GUI plugin for displaying and replaying ROS bag
files.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.4-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.4-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.4-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.5.1-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.4-1
- Initial humble build
