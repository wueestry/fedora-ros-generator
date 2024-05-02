# Meta Package
Name:           ros-humble-rqt-service-caller
Version:        1.0.5
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_service_caller
Summary:        Meta package for ros2-humble-rqt_service_caller and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rqt_service_caller
Requires:       ros2-humble-rqt_service_caller-devel

Obsoletes: ros-humble-rqt-service-caller < 1.0.5-1

%description
rqt_service_caller provides a GUI plugin for calling arbitrary
services.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.5-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.5-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.5-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.4.10-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.5-1
- Initial humble build
