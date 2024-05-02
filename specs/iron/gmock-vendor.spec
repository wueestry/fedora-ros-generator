# Meta Package
Name:           ros-iron-gmock-vendor
Version:        1.10.9005
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-gmock_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-gmock_vendor
Requires:       ros2-iron-gmock_vendor-devel

Obsoletes: ros-iron-gmock-vendor < 1.10.9005-1

%description
The package provides GoogleMock.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.10.9005-1
- Update to latest release
