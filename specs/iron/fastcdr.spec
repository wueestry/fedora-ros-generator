# Meta Package
Name:           ros-iron-fastcdr
Version:        1.0.27
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-fastcdr and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-fastcdr
Requires:       ros2-iron-fastcdr-devel

Obsoletes: ros-iron-fastcdr < 1.0.27-1

%description
CDR serialization implementation.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.0.27-1
- Update to latest release
