# Meta Package
Name:           ros-humble-osqp-vendor
Version:        0.2.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/oxfordcontrol/osqp
Summary:        Meta package for ros2-humble-osqp_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-osqp_vendor
Requires:       ros2-humble-osqp_vendor-devel

Obsoletes: ros-humble-osqp-vendor < 0.2.0-1

%description
Wrapper around osqp that ships with a CMake module

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 05 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.2.0-1
- Update to latest release
