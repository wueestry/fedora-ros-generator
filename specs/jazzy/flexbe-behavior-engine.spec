# Meta Package
Name:           ros-jazzy-flexbe-behavior-engine
Version:        3.0.3
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-flexbe_behavior_engine and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-flexbe_behavior_engine
Requires:       ros2-jazzy-flexbe_behavior_engine-devel

Obsoletes: ros-jazzy-flexbe-behavior-engine < 3.0.3-1

%description
A meta-package to aggregate all the FlexBE packages

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Oct 15 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.0.3-1
- Update to latest release
