# Meta Package
Name:           ros-jazzy-rqt-service-caller
Version:        1.2.1
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_service_caller
Summary:        Meta package for ros2-jazzy-rqt_service_caller and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rqt_service_caller
Requires:       ros2-jazzy-rqt_service_caller-devel

Obsoletes: ros-jazzy-rqt-service-caller < 1.2.1-1

%description
rqt_service_caller provides a GUI plugin for calling arbitrary
services.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.2.1-1
- Update to latest release
