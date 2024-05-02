# Meta Package
Name:           ros-humble-rqt-publisher
Version:        1.5.0
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_publisher
Summary:        Meta package for ros2-humble-rqt_publisher and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rqt_publisher
Requires:       ros2-humble-rqt_publisher-devel

Obsoletes: ros-humble-rqt-publisher < 1.5.0-1

%description
rqt_publisher provides a GUI plugin for publishing arbitrary messages
with fixed or computed field values.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.5.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.5.0-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.5.0-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.4.10-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.5.0-1
- Initial humble build
